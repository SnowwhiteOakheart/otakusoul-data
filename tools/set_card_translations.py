#!/usr/bin/env python3
"""Writes translations of character cards (`data.extensions.otakusoul_i18n.translations.<lang>`).

Input: JSON object `{"<card name>": {"<lang>": {"description": …, "first_mes": …, …}}}`. The fields
replace the card's translation for that language (other languages stay as they are). Every card of
that name gets it: profile JSON, preset PNG and hub PNG (`cards_gateway/`); in PNG files only the
`chara`/`ccv3` text chunk is replaced, the picture stays byte for byte (helpers from
`set_card_voices.py`). Afterwards raise the cards' `revision` in `soul_registry.json`.

    python3 tools/set_card_translations.py uebersetzungen.json [--check]
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from set_card_voices import CARD_CHUNKS, ROOT, card_files, dump_like, png_chunks, text_chunk  # noqa: E402

I18N_KEY = "otakusoul_i18n"
LANGS = {"de", "en", "ru", "ja"}
FIELDS = {
    "name", "custom_title", "description", "personality", "scenario", "first_mes", "alternate_greetings",
    "mes_example", "system_prompt", "post_history_instructions", "creator_notes", "tags",
}


def with_translations(card: dict, translations: dict[str, dict]) -> bool:
    """Sets the translations on a card; returns whether anything changed."""
    data = card.get("data")
    if not isinstance(data, dict):
        return False
    i18n = data.setdefault("extensions", {}).setdefault(I18N_KEY, {})
    existing = i18n.setdefault("translations", {})
    changed = False
    for lang, fields in translations.items():
        if existing.get(lang) != fields:
            existing[lang] = fields
            changed = True
    return changed


def update_json(path: Path, wanted: dict, write: bool) -> str | None:
    original = path.read_text(encoding="utf-8")
    try:
        card = json.loads(original)
    except json.JSONDecodeError:
        return None
    if not isinstance(card, dict) or card.get("spec") != "chara_card_v2":
        return None
    name = card.get("data", {}).get("name")
    if name not in wanted:
        return None
    if with_translations(card, wanted[name]) and write:
        path.write_text(dump_like(original, card), encoding="utf-8", newline="")
    return name


def update_png(path: Path, wanted: dict, write: bool) -> str | None:
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
        if name not in wanted:
            continue
        found = name
        if not with_translations(card, wanted[name]):
            continue
        encoded = base64.b64encode(dump_like(payload, card).encode("utf-8")).decode("ascii")
        pieces += [raw[last:start], text_chunk(keyword, encoded)]
        last = end
        changed = True
    if changed and write:
        pieces.append(raw[last:])
        path.write_bytes(b"".join(pieces))
    return found


def check_input(wanted: dict) -> list[str]:
    problems = []
    for name, translations in wanted.items():
        for lang, fields in translations.items():
            if lang not in LANGS:
                problems.append(f"{name}: unbekannte Sprache {lang!r}")
            unknown = set(fields) - FIELDS
            if unknown:
                problems.append(f"{name} [{lang}]: unbekannte Felder {sorted(unknown)}")
            for key in ("first_mes", "mes_example", "system_prompt"):
                if key in fields and fields[key].count("{{") != fields[key].count("}}"):
                    problems.append(f"{name} [{lang}]: {key} mit kaputtem Platzhalter")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("translations", type=Path, help="JSON: card name -> language -> fields")
    parser.add_argument("--check", action="store_true", help="only report, write nothing")
    args = parser.parse_args()
    wanted = json.loads(args.translations.read_text(encoding="utf-8"))
    problems = check_input(wanted)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    seen: dict[str, list[str]] = {}
    for path in card_files():
        handler = update_png if path.suffix.lower() == ".png" else update_json
        name = handler(path, wanted, write=not args.check)
        if name:
            seen.setdefault(name, []).append(str(path.relative_to(ROOT)).replace("\\", "/"))
    for name in sorted(seen):
        print(f"{name}: {len(seen[name])} Datei(en)")
    missing = sorted(set(wanted) - set(seen))
    if missing:
        print("Keine Karte gefunden für:", ", ".join(missing), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
