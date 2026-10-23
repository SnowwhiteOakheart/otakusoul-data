#!/usr/bin/env python3
"""Sets the voice description of character cards (`data.extensions.otakusoul_voice`).

OtakuSoul uses the description for Qwen3-TTS VoiceDesign and OpenAI speech while a character's
voice settings have no description of their own. Write it in English: age, timbre, pace, mood.

The voices come from a JSON object `{ "<card name>": "<description>", ... }` (the name as in
`data.name`). Every card with that name is updated: preset JSON, preset PNG and gateway PNG.
JSON files keep their formatting; in PNG files only the `chara`/`ccv3` text chunk is replaced,
the image data stays byte for byte.

    python3 tools/set_card_voices.py voices.json          # write
    python3 tools/set_card_voices.py voices.json --check  # only report what would change

Without Pillow; only the standard library.
"""

from __future__ import annotations

import argparse
import base64
import json
import struct
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCAN_DIRS = ("presets", "cards_gateway")
SKIP_DIRS = {"expressions", "backgrounds", ".git", ".venv"}
VOICE_KEY = "otakusoul_voice"
CARD_CHUNKS = (b"chara", b"ccv3")


def with_voice(card: dict, description: str) -> bool:
    """Sets the voice on a card; returns whether anything changed."""
    data = card.get("data")
    if not isinstance(data, dict):
        return False
    extensions = data.setdefault("extensions", {})
    wanted = {"description": description}
    if extensions.get(VOICE_KEY) == wanted:
        return False
    extensions[VOICE_KEY] = wanted
    return True


def dump_like(original: str, value: dict) -> str:
    """Serialises `value` the way `original` was written (indent, escaping, final newline)."""
    lines = original.splitlines()
    indent = None
    if len(lines) > 1:
        stripped = lines[1].lstrip(" ")
        indent = len(lines[1]) - len(stripped) or None
    ensure_ascii = all(ord(c) < 128 for c in original) and "\\u" in original
    if indent is None:
        text = json.dumps(value, ensure_ascii=ensure_ascii, separators=(",", ":"))
    else:
        text = json.dumps(value, ensure_ascii=ensure_ascii, indent=indent)
    return text + ("\n" if original.endswith("\n") else "")


def update_json(path: Path, voices: dict[str, str], write: bool) -> str | None:
    original = path.read_text(encoding="utf-8")
    try:
        card = json.loads(original)
    except json.JSONDecodeError:
        return None
    if not isinstance(card, dict) or card.get("spec") != "chara_card_v2":
        return None
    name = card.get("data", {}).get("name")
    if name not in voices or not with_voice(card, voices[name]):
        return name if name in voices else None
    if write:
        path.write_text(dump_like(original, card), encoding="utf-8", newline="")
    return name


def png_chunks(raw: bytes):
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        return
    offset = 8
    while offset + 8 <= len(raw):
        (length,) = struct.unpack(">I", raw[offset : offset + 4])
        kind = raw[offset + 4 : offset + 8]
        end = offset + 12 + length
        yield offset, end, kind, raw[offset + 8 : offset + 8 + length]
        offset = end


def text_chunk(keyword: bytes, text: str) -> bytes:
    body = keyword + b"\x00" + text.encode("latin-1")
    return (
        struct.pack(">I", len(body))
        + b"tEXt"
        + body
        + struct.pack(">I", zlib.crc32(b"tEXt" + body) & 0xFFFFFFFF)
    )


def update_png(path: Path, voices: dict[str, str], write: bool) -> str | None:
    raw = path.read_bytes()
    pieces: list[bytes] = []
    last = 0
    found = None
    changed = False
    for start, end, kind, body in png_chunks(raw) or ():
        if kind != b"tEXt":
            continue
        keyword, _, value = body.partition(b"\x00")
        if keyword not in CARD_CHUNKS:
            continue
        payload = base64.b64decode(value).decode("utf-8")
        card = json.loads(payload)
        name = card.get("data", {}).get("name")
        if name not in voices:
            continue
        found = name
        if not with_voice(card, voices[name]):
            continue
        encoded = base64.b64encode(dump_like(payload, card).encode("utf-8")).decode("ascii")
        pieces += [raw[last:start], text_chunk(keyword, encoded)]
        last = end
        changed = True
    if changed and write:
        pieces.append(raw[last:])
        path.write_bytes(b"".join(pieces))
    return found


def card_files():
    for directory in SCAN_DIRS:
        for path in sorted((ROOT / directory).rglob("*")):
            if path.is_file() and not SKIP_DIRS.intersection(path.relative_to(ROOT).parts):
                if path.suffix.lower() in (".json", ".png"):
                    yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("voices", type=Path, help="JSON object: card name -> voice description")
    parser.add_argument("--check", action="store_true", help="only report, write nothing")
    args = parser.parse_args()
    voices = json.loads(args.voices.read_text(encoding="utf-8"))
    seen: dict[str, list[str]] = {}
    for path in card_files():
        handler = update_png if path.suffix.lower() == ".png" else update_json
        name = handler(path, voices, write=not args.check)
        if name:
            seen.setdefault(name, []).append(str(path.relative_to(ROOT)).replace("\\", "/"))
    for name in sorted(seen):
        print(f"{name}: {len(seen[name])} Datei(en)")
    missing = sorted(set(voices) - set(seen))
    if missing:
        print("Keine Karte gefunden für:", ", ".join(missing), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
