#!/usr/bin/env python3
"""
Orchestrator: Sends chunks to Gemini 2.5 Flash API in parallel,
stores structured JSON analysis for each chunk.
Supports progress saving and auto-resume.
"""

import asyncio
import json
import os
import sys
import aiohttp
from tqdm import tqdm

API_URL = "http://31.77.19.35:8899/v1/chat/completions"
API_KEY = "Bz9ZrOY-hR1OytPej6ijYJH0HeqU4-5zMli4kKgRnok"
# Failover fallback list of groups/models on the proxy if one returns 404
BACKUPS = [
    {"group": "Gemini(Vertex)", "model": "gemini-2.5-flash"},
    {"group": "Gemini(Antigravity)", "model": "gemini-3.8-flash"},
    {"group": "Gemini(Antigravity)2", "model": "gemini-2.5-flash"}
]

BASE_DIR = "/home/levels/projects/knowledge_base"
MANIFEST_FILE = os.path.join(BASE_DIR, "data/chunks_manifest.json")
RESULTS_DIR = os.path.join(BASE_DIR, "data/analysis")
PROGRESS_FILE = os.path.join(BASE_DIR, "data/progress.json")

STATE_FILE = os.path.join(BASE_DIR, "data/current_state.json")

def load_current_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"last_updated_chunk": 0, "technologies": {}}

def save_current_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def format_state_for_prompt(state):
    techs = state.get("technologies", {})
    if not techs:
        return "Текущая база знаний пока пуста (это начальные чанки хронологии)."
    
    lines = ["Текущее известное состояние технологий (из предыдущих чанков):"]
    for tech, info in techs.items():
        status = info.get("status", "неизвестно")
        last_details = info.get("last_details", "")
        last_chunk = info.get("last_chunk", "")
        lines.append(f"- **{tech}**: статус [{status}]. Последние сведения: {last_details} (зафиксировано в чанке {last_chunk})")
    return "\n".join(lines)

def update_state_with_chunk(state, chunk_num, chunk_analysis):
    techs = state.setdefault("technologies", {})
    updates = chunk_analysis.get("status_updates", [])
    for u in updates:
        tech_name = u.get("tech", "").strip()
        if not tech_name:
            continue
        new_status = u.get("new_status", "под вопросом")
        details = u.get("details", "")
        msg_id = u.get("msg_id")

        if tech_name not in techs:
            techs[tech_name] = {
                "status": new_status,
                "history": [],
                "last_details": details,
                "last_chunk": chunk_num,
                "last_msg_id": msg_id
            }
        else:
            prev_status = techs[tech_name].get("status")
            techs[tech_name]["status"] = new_status
            techs[tech_name]["last_details"] = details
            techs[tech_name]["last_chunk"] = chunk_num
            techs[tech_name]["last_msg_id"] = msg_id

        techs[tech_name].setdefault("history", []).append({
            "chunk": chunk_num,
            "msg_id": msg_id,
            "from_status": u.get("previous_status"),
            "to_status": new_status,
            "change_type": u.get("change_type"),
            "details": details
        })
    state["last_updated_chunk"] = chunk_num

SYSTEM_PROMPT = """Ты — ведущий эксперт и аналитик по обходу цензуры, DPI, ТСПУ (РКН), сетевым протоколам и VPN-решениям в рунете.
Тебе предоставлена:
1. ТЕКУЩАЯ БАЗА ЗНАНИЙ (хронологическое состояние технологий на момент прошлого чанка: что работало, что ломалось, что тестировалось).
2. НОВАЯ ПАЧКА СООБЩЕНИЙ из сообщества openlibrecommunity.

Твоя ключевая задача:
- Анализировать НОВУЮ пачку с учетом ПРЕДЫДУЩЕГО состояния.
- Отслеживать ИЗМЕНЕНИЯ СТАТУСА:
  * Если что-то раньше работало, а теперь в сообщениях пишут, что заблокировали/сломалось -> зафиксируй смену статуса!
  * Если что-то раньше не работало или было под вопросом, а теперь починили/нашли рабочий конфиг/стратегию -> зафиксируй переход в «работает»!
  * Если повторяется старая информация без новых деталей -> не дублируй избыточно, отметь только если это подтверждает устойчивость метода.

Формат ответа — СТРОГИЙ JSON:
{
  "title": "Краткий емкий заголовок темы обсуждения в этом чанке (до 10 слов)",
  "summary": "Краткое саммари обсуждения (2-4 предложения): о чем говорили, какие проблемы решали",
  "technologies": ["список упомянутых технологий/софта/протоколов/провайдеров"],
  "status_updates": [
    {
      "tech": "Название технологии/инструмента (например: VLESS Reality, NaiveProxy, zapret, AmneziaWG)",
      "previous_status": "работало | не работало | под вопросом | новое",
      "new_status": "работает | не работает | под вопросом",
      "change_type": "status_changed | confirmed | new_finding | details_added",
      "details": "Что изменилось или подтвердилось (причина блокировки, новый флаг, фикс, поведение у провайдера)",
      "msg_id": 12345
    }
  ],
  "notable_messages": [
    {
      "msg_id": 12345,
      "reason": "Почему важно: полезный конфиг / решение проблемы / инсайт по ТСПУ / фикс"
    }
  ]
}

ВАЖНО:
- Указывай ТОЛЬКО реальные msg_id из текста сообщений (числа из тегов msg_XXXX).
- Отвечай ТОЛЬКО валидным JSON без markdown оберток (без ```json ... ```)."""

async def process_chunk(session, chunk_info, state_context):
    chunk_num = chunk_info["chunk_num"]
    result_path = os.path.join(RESULTS_DIR, f"chunk_{chunk_num:04d}.json")

    if os.path.exists(result_path):
        with open(result_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except Exception:
                pass

    # Read chunk text (truncate if huge to avoid proxy timeouts)
    chunk_file = chunk_info["path"]
    with open(chunk_file, "r", encoding="utf-8") as f:
        content = f.read()

    if len(content) > 30000:
        content = content[:30000] + "\n...[truncated for length]..."

    user_prompt = f"""=== ТЕКУЩИЙ КОНТЕКСТ ЗНАНИЙ (RAG ИЗ ПРОШЛЫХ ЧАНКОВ) ===
{state_context}

=== НОВАЯ ПАЧКА СООБЩЕНИЙ ЧАНКА #{chunk_num} ===
{content}"""

    retries = 3
    for backup_cfg in BACKUPS:
        cur_group = backup_cfg["group"]
        cur_model = backup_cfg["model"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
            "X-DDT-Group": cur_group
        }
        payload = {
            "model": cur_model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.2,
            "max_tokens": 4096
        }

        for attempt in range(retries):
            try:
                async with session.post(API_URL, headers=headers, json=payload, timeout=aiohttp.ClientTimeout(total=90)) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        text_res = data["choices"][0]["message"]["content"].strip()
                        if text_res.startswith("```"):
                            text_res = text_res.strip("`")
                            if text_res.startswith("json"):
                                text_res = text_res[4:].strip()
                        # Extract first JSON object if surrounded by extra text
                        import re
                        m = re.search(r"\{.*\}", text_res, re.DOTALL)
                        if m:
                            text_res = m.group(0)
                        parsed = json.loads(text_res)
                        parsed["chunk_num"] = chunk_num
                        parsed["start_id"] = chunk_info["start_id"]
                        parsed["end_id"] = chunk_info["end_id"]
                        parsed["date_range"] = f"{chunk_info['start_date']} — {chunk_info['end_date']}"

                        with open(result_path, "w", encoding="utf-8") as out_f:
                            json.dump(parsed, out_f, ensure_ascii=False, indent=2)
                        return parsed
                    else:
                        err_text = await resp.text()
                        if "404" in str(resp.status):
                            # Upstream project in this group died, break to next backup group
                            break
                        if attempt == retries - 1:
                            print(f"[Chunk {chunk_num}] ({cur_group}) HTTP {resp.status}: {err_text[:100]}")
            except Exception as e:
                if attempt == retries - 1:
                    print(f"[Chunk {chunk_num}] Error: {e}")
            await asyncio.sleep(2 * (attempt + 1))
    return None

async def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    # Check which chunks are missing
    existing_chunks = set()
    for f in os.listdir(RESULTS_DIR):
        if f.startswith("chunk_") and f.endswith(".json"):
            try:
                num = int(f.replace("chunk_", "").replace(".json", ""))
                existing_chunks.add(num)
            except ValueError:
                pass

    manifest = [c for c in manifest if c["chunk_num"] not in existing_chunks]

    state = load_current_state()
    print(f"Orchestrator running for {len(manifest)} missing chunks...")
    print(f"Known technologies in state memory: {len(state.get('technologies', {}))}")

    connector = aiohttp.TCPConnector(limit=3)
    async with aiohttp.ClientSession(connector=connector) as session:
        with tqdm(total=len(manifest), desc="Processing missing chunks (RAG)") as pbar:
            for chunk_info in manifest:
                c_num = chunk_info["chunk_num"]
                state_context = format_state_for_prompt(state)
                res = await process_chunk(session, chunk_info, state_context)
                if res:
                    update_state_with_chunk(state, c_num, res)
                    save_current_state(state)
                pbar.update(1)

    print("Missing chunks run complete!")
    print(f"Final state updated: {len(state.get('technologies', {}))} technologies tracked.")

if __name__ == "__main__":
    asyncio.run(main())
