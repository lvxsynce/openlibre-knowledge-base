#!/usr/bin/env python3
"""
Step 1: Parse result.json, filter noise/service messages, and split into chunks of ~300 meaningful messages.
Generates chunk_XXXX.md files with local anchors <a id="msg_XXXX"></a>.
"""

import json
import os
import re

INPUT_FILE = "/home/levels/projects/ChatExport_2026-10-26/result.json"
OUTPUT_DIR = "/home/levels/projects/knowledge_base/chunks"
CHUNK_SIZE = 300

# Stop-words / spam regex to filter out 1-word useless messages
USELESS_EXACT = {
    "да", "нет", "ок", "не", "ага", "пон", "ладно", "хз", "лол", "кек",
    "+", "-", "!", "?", "👍", "👎", "🤣", "😂", "спасибо", "спс", "жиза", "база",
    "анлак", "понял", "ясн", "ясно"
}

def clean_text(raw_text):
    if isinstance(raw_text, str):
        return raw_text.strip()
    if isinstance(raw_text, list):
        parts = []
        for item in raw_text:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict) and "text" in item:
                parts.append(item["text"])
        return "".join(parts).strip()
    return ""

def is_meaningful(msg):
    if msg.get("type") != "message":
        return False
    text = clean_text(msg.get("text", ""))
    if not text:
        return False
    # If text is too short and in useless list
    cleaned_lower = text.lower().strip()
    if cleaned_lower in USELESS_EXACT:
        return False
    if len(cleaned_lower) <= 2 and not any(c.isdigit() or c.isalpha() for c in cleaned_lower):
        return False
    return True

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Reading {INPUT_FILE}...")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    messages = data.get("messages", [])
    print(f"Total raw items: {len(messages)}")

    meaningful_msgs = []
    for m in messages:
        if is_meaningful(m):
            text = clean_text(m.get("text", ""))
            author = m.get("from") or m.get("actor") or "Unknown"
            meaningful_msgs.append({
                "id": m["id"],
                "date": m.get("date", ""),
                "author": author,
                "reply_to": m.get("reply_to_message_id"),
                "text": text
            })

    total_meaningful = len(meaningful_msgs)
    print(f"Meaningful messages after filter: {total_meaningful}")

    chunks_count = (total_meaningful + CHUNK_SIZE - 1) // CHUNK_SIZE
    print(f"Splitting into {chunks_count} chunks (size {CHUNK_SIZE})...")

    manifest = []

    for i in range(chunks_count):
        batch = meaningful_msgs[i * CHUNK_SIZE : (i + 1) * CHUNK_SIZE]
        chunk_num = i + 1
        chunk_filename = f"chunk_{chunk_num:04d}.md"
        chunk_path = os.path.join(OUTPUT_DIR, chunk_filename)

        start_id = batch[0]["id"]
        end_id = batch[-1]["id"]
        start_date = batch[0]["date"]
        end_date = batch[-1]["date"]

        lines = [
            f"# Чанк {chunk_num:04d}",
            f"**Сообщения:** с #{start_id} по #{end_id} (всего {len(batch)})",
            f"**Период:** {start_date} — {end_date}",
            "",
            "---",
            ""
        ]

        for m in batch:
            m_id = m["id"]
            author = m["author"]
            date = m["date"]
            reply_str = f" (в ответ на #{m['reply_to']})" if m['reply_to'] else ""
            lines.append(f'<a id="msg_{m_id}"></a>')
            lines.append(f"### [msg_{m_id}](chunk_{chunk_num:04d}.md#msg_{m_id}) | {date} | {author}{reply_str}")
            # Escape code blocks if needed, indent
            lines.append(m["text"])
            lines.append("")

        with open(chunk_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        manifest.append({
            "chunk_num": chunk_num,
            "filename": chunk_filename,
            "count": len(batch),
            "start_id": start_id,
            "end_id": end_id,
            "start_date": start_date,
            "end_date": end_date,
            "path": chunk_path
        })

    manifest_path = "/home/levels/projects/knowledge_base/data/chunks_manifest.json"
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"Done! {chunks_count} chunks written to {OUTPUT_DIR}")
    print(f"Manifest written to {manifest_path}")

if __name__ == "__main__":
    main()
