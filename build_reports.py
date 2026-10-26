#!/usr/bin/env python3
"""
Step 3: Aggregator and Reporter.
Reads all chunk analysis JSONs and builds two master markdown files:
1. status_report.md - What works, what is broken, what is questionable (categorized + linked).
2. index_catalog.md - Fast memory register for LLM (Topic -> Summary -> Local chunk link).
"""

import json
import os
import glob
from collections import defaultdict

BASE_DIR = "/home/levels/projects/knowledge_base"
ANALYSIS_DIR = os.path.join(BASE_DIR, "data/analysis")
CHUNKS_DIR = "chunks"

STATUS_REPORT_FILE = os.path.join(BASE_DIR, "status_report.md")
INDEX_CATALOG_FILE = os.path.join(BASE_DIR, "index_catalog.md")

def main():
    json_files = sorted(glob.glob(os.path.join(ANALYSIS_DIR, "chunk_*.json")))
    if not json_files:
        print("No analysis files found!")
        return

    print(f"Aggregating {len(json_files)} analysis files...")

    # Load persistent state
    state_file = os.path.join(BASE_DIR, "data/current_state.json")
    state = {}
    if os.path.exists(state_file):
        with open(state_file, "r", encoding="utf-8") as f:
            state = json.load(f)

    all_chunks = []
    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            try:
                all_chunks.append(json.load(f))
            except Exception as e:
                print(f"Error reading {jf}: {e}")

    techs = state.get("technologies", {})

    works_group = []
    broken_group = []
    questionable_group = []

    for t_name, info in techs.items():
        st = info.get("status", "").lower()
        if "работает" in st and "не" not in st:
            works_group.append((t_name, info))
        elif "не работает" in st:
            broken_group.append((t_name, info))
        else:
            questionable_group.append((t_name, info))

    report_lines = [
        "# Сводный статус решений и технологий (openlibrecommunity)",
        f"**Обработано пачек:** {len(all_chunks)} | **Отслеживаемых технологий в памяти:** {len(techs)}",
        "",
        "> Отчет формируется последовательным RAG-анализом: модель помнит прошлые статусы и фиксирует изменения во времени.",
        "> Для каждой технологии приведена хронология изменения статусов (с указанием чанков и сообщений).",
        "",
        "---",
        "",
        "## 🟢 РАБОТАЕТ В НАСТОЯЩИЙ МОМЕНТ (Подтвержденные актуальные методы)",
        ""
    ]

    def render_tech_block(group):
        lines = []
        if not group:
            lines.append("_Нет данных._\n")
            return lines

        for t_name, info in group:
            last_chunk = info.get("last_chunk", 1)
            last_msg = info.get("last_msg_id")
            last_link = f"[{t_name} в chunk_{last_chunk:04d}.md#msg_{last_msg}]({CHUNKS_DIR}/chunk_{last_chunk:04d}.md#msg_{last_msg})" if last_msg else f"chunk_{last_chunk:04d}.md"
            lines.append(f"### {t_name}")
            lines.append(f"- **Текущее состояние:** {info.get('last_details', '')}")
            lines.append(f"- **Последнее подтверждение:** {last_link}")
            lines.append("- **Хронология эволюции:**")
            for h in info.get("history", []):
                c_num = h.get("chunk", 1)
                m_id = h.get("msg_id")
                link = f"[{CHUNKS_DIR}/chunk_{c_num:04d}.md#msg_{m_id}]({CHUNKS_DIR}/chunk_{c_num:04d}.md#msg_{m_id})" if m_id else f"chunk_{c_num:04d}.md"
                f_st = h.get("from_status")
                t_st = h.get("to_status")
                lines.append(f"  * `[Чанк {c_num:04d}]` ({f_st} -> **{t_st}**): {h.get('details')} | Ссылка: {link}")
            lines.append("")
        return lines

    report_lines.extend(render_tech_block(works_group))

    report_lines.extend([
        "---",
        "",
        "## 🔴 НЕ РАБОТАЕТ / ЗАБЛОКИРОВАНО ТСПУ",
        ""
    ])
    report_lines.extend(render_tech_block(broken_group))

    report_lines.extend([
        "---",
        "",
        "## 🟡 ПОД ВОПРОСОМ / ТЕСТИРУЕТСЯ / ПЛАВАЮЩИЙ СТАТУС",
        ""
    ])
    report_lines.extend(render_tech_block(questionable_group))

    with open(STATUS_REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    # Build FILE 2: index_catalog.md
    index_lines = [
        "# Реестр-память обсуждений сообщества",
        "**Назначение:** Быстрый поиск тем и переход к точным пачкам сообщений для нейросети.",
        "",
        "| Пачка | Период | Сообщения | Тема | Краткое содержание | Технологии |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |"
    ]

    for c in all_chunks:
        c_num = c.get("chunk_num", 1)
        c_file = f"chunk_{c_num:04d}.md"
        c_link = f"[{c_file}]({CHUNKS_DIR}/{c_file})"
        date_rng = c.get("date_range", "")
        msgs_rng = f"#{c.get('start_id')}–#{c.get('end_id')}"
        title = c.get("title", "").replace("|", "/")
        summary = c.get("summary", "").replace("|", "/")
        techs = ", ".join(c.get("technologies", []))

        index_lines.append(f"| {c_link} | {date_rng} | {msgs_rng} | **{title}** | {summary} | `{techs}` |")

    # Add notable configs section
    index_lines.extend([
        "",
        "---",
        "",
        "## Ключевые сообщения и полезные находки (конфиги, дампы, инсайты):",
        ""
    ])

    for c in all_chunks:
        c_num = c.get("chunk_num", 1)
        c_file = f"chunk_{c_num:04d}.md"
        for n in c.get("notable_messages", []):
            m_id = n.get("msg_id")
            reason = n.get("reason", "")
            index_lines.append(f"- [{c_file}#msg_{m_id}]({CHUNKS_DIR}/{c_file}#msg_{m_id}): {reason}")

    with open(INDEX_CATALOG_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines))

    print(f"Reports successfully generated:")
    print(f" -> {STATUS_REPORT_FILE}")
    print(f" -> {INDEX_CATALOG_FILE}")

if __name__ == "__main__":
    main()
