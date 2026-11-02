#!/usr/bin/env python3
"""Sets the music settings (`extensions.otakusoul_music`) of scenes, lorebooks and character cards.

OtakuSoul generates a story's mood music with ACE-Step from these settings and plays it in the
Stage (schema: `docs/stage_music.md` in the app repository):

- scene:    {"set", "style", "moods": {"<mood>": {"caption", "lyrics", "vocal_language", "bpm",
            "duration", "count", ...}}, "tracks": [...]} – all scenes of a story share one set
- lorebook: {"style"} – the sound of a world, inherited by scenes without a style of their own
- card:     {"theme", "moods"} – a leitmotif joined to those moods while the character plays

The settings come from a JSON manifest:

    {"scenes":    {"<registry scene id>": {...}},
     "lorebooks": {"<lorebook name>": {...}},
     "cards":     {"<card name>": {...}}}

Every file of an entry is updated: gateway and preset copies of scenes (matched by title),
lorebooks (by name) and cards (by `data.name`: preset JSON, preset PNG and gateway PNG; in PNG
files only the `chara`/`ccv3` text chunk is replaced). Registry entries whose files changed get
`revision` + 1 and today's `updated`, so installed copies receive the update.

    python3 tools/set_music.py music.json            # write
    python3 tools/set_music.py music.json --check    # only report
    python3 tools/set_music.py music.json --root ../OtakuSoul   # another repository (no registries there)

Only the standard library.
"""

from __future__ import annotations

import argparse
import base64
import datetime
import json
import struct
import sys
import zlib
from pathlib import Path

MUSIC_KEY = "otakusoul_music"
CARD_CHUNKS = (b"chara", b"ccv3")
SKIP_DIRS = {"expressions", "backgrounds", ".git", ".venv", "node_modules", "music"}
MOODS = {"calm", "tavern", "adventure", "tension", "mystery", "combat", "boss", "romance", "sorrow"}


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


def set_music(holder: dict, music: dict) -> bool:
    """Puts `music` into `holder["extensions"]`; returns whether anything changed."""
    extensions = holder.get("extensions")
    if not isinstance(extensions, dict):
        extensions = {}
        holder["extensions"] = extensions
    if extensions.get(MUSIC_KEY) == music:
        return False
    extensions[MUSIC_KEY] = music
    return True


def check_manifest(manifest: dict) -> list[str]:
    problems = []
    for sid, music in manifest.get("scenes", {}).items():
        for mood, spec in music.get("moods", {}).items():
            if mood not in MOODS:
                problems.append(f"Szene {sid}: unbekannte Stimmung {mood}")
            if not spec.get("caption"):
                problems.append(f"Szene {sid}/{mood}: caption fehlt")
            if spec.get("lyrics") and spec.get("lyrics") != "[Instrumental]" and not spec.get("vocal_language"):
                problems.append(f"Szene {sid}/{mood}: Lyrics ohne vocal_language")
        if not music.get("set"):
            problems.append(f"Szene {sid}: set fehlt")
    for name, music in manifest.get("cards", {}).items():
        if not music.get("theme"):
            problems.append(f"Karte {name}: theme fehlt")
        for mood in music.get("moods", []):
            if mood not in MOODS:
                problems.append(f"Karte {name}: unbekannte Stimmung {mood}")
    for name, music in manifest.get("lorebooks", {}).items():
        if not music.get("style"):
            problems.append(f"Lorebook {name}: style fehlt")
    return problems


def json_files(root: Path, dirs: tuple[str, ...]):
    for directory in dirs:
        base = root / directory
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.json")):
            if not SKIP_DIRS.intersection(path.relative_to(root).parts[:-1]):
                yield path


def update_json_file(path: Path, pick, write: bool) -> str | None:
    """`pick(content)` returns (key, music) for files to update; returns the key if it matched."""
    original = path.read_text(encoding="utf-8")
    try:
        content = json.loads(original)
    except json.JSONDecodeError:
        return None
    if not isinstance(content, dict):
        return None
    picked = pick(content)
    if not picked:
        return None
    key, music, holder = picked
    changed = set_music(holder, music)
    if changed and write:
        path.write_text(dump_like(original, content), encoding="utf-8", newline="")
    return key if changed else None


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


def update_png(path: Path, cards: dict, write: bool, matched: set[str]) -> str | None:
    raw = path.read_bytes()
    pieces: list[bytes] = []
    last = 0
    changed_name = None
    for start, end, kind, body in png_chunks(raw) or ():
        if kind != b"tEXt":
            continue
        keyword, _, value = body.partition(b"\x00")
        if keyword not in CARD_CHUNKS:
            continue
        payload = base64.b64decode(value).decode("utf-8")
        card = json.loads(payload)
        data = card.get("data")
        name = data.get("name") if isinstance(data, dict) else None
        if name not in cards:
            continue
        matched.add(name)
        if not set_music(data, cards[name]):
            continue
        encoded = base64.b64encode(dump_like(payload, card).encode("utf-8")).decode("ascii")
        pieces += [raw[last:start], text_chunk(keyword, encoded)]
        last = end
        changed_name = name
    if changed_name and write:
        pieces.append(raw[last:])
        path.write_bytes(b"".join(pieces))
    return changed_name


def bump(root: Path, registry: str, list_key: str, key_field: str, keys: set[str], write: bool) -> list[str]:
    path = root / registry
    if not path.is_file() or not keys:
        return []
    original = path.read_text(encoding="utf-8")
    content = json.loads(original)
    today = datetime.date.today().isoformat()
    bumped = []
    for entry in content.get(list_key, []):
        if entry.get(key_field) in keys:
            entry["revision"] = int(entry.get("revision", 1)) + 1
            entry["updated"] = today
            bumped.append(entry[key_field])
    if bumped and write:
        path.write_text(dump_like(original, content), encoding="utf-8", newline="")
    return bumped


def scene_titles(root: Path, scenes: dict) -> dict[str, str]:
    """Registry scene id -> title of its gateway file (preset copies carry the same title)."""
    path = root / "stages_registry.json"
    titles = {}
    if not path.is_file():
        return titles
    for entry in json.loads(path.read_text(encoding="utf-8")).get("scenes", []):
        if entry.get("id") not in scenes:
            continue
        relative = entry.get("download_url", "").split("/main/", 1)[-1]
        try:
            titles[entry["id"]] = json.loads((root / relative).read_text(encoding="utf-8"))["title"]
        except (OSError, KeyError, json.JSONDecodeError):
            print(f"FEHLER: Szenendatei für {entry['id']} nicht lesbar ({relative})")
    return titles


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("manifest", type=Path, help="JSON: scenes / lorebooks / cards")
    parser.add_argument("--check", action="store_true", help="only report, write nothing")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    problems = check_manifest(manifest)
    for problem in problems:
        print(f"FEHLER: {problem}")
    if problems:
        return 1
    write = not args.check
    scenes = manifest.get("scenes", {})
    lorebooks = manifest.get("lorebooks", {})
    cards = manifest.get("cards", {})

    # Scenes: by the title of the registry's file (gateway and preset copies alike).
    titles = scene_titles(root, scenes)
    by_title = {title: sid for sid, title in titles.items()}
    changed_scenes: set[str] = set()
    found_scenes: set[str] = set()

    def pick_scene(content: dict):
        sid = by_title.get(content.get("title")) if "gm_tone" in content else None
        if sid is None:
            return None
        found_scenes.add(sid)
        return sid, scenes[sid], content

    changed_lorebooks: set[str] = set()
    found_lorebooks: set[str] = set()

    def pick_lorebook(content: dict):
        name = content.get("name")
        if "entries" not in content or name not in lorebooks:
            return None
        found_lorebooks.add(name)
        return name, lorebooks[name], content

    changed_cards: set[str] = set()
    found_cards: set[str] = set()

    def pick_card(content: dict):
        data = content.get("data")
        if content.get("spec") != "chara_card_v2" or not isinstance(data, dict):
            return None
        name = data.get("name")
        if name not in cards:
            return None
        found_cards.add(name)
        return name, cards[name], data

    for path in json_files(root, ("stages_gateway", "presets")):
        if (key := update_json_file(path, pick_scene, write)):
            changed_scenes.add(key)
    for path in json_files(root, ("lorebooks_gateway", "presets")):
        if (key := update_json_file(path, pick_lorebook, write)):
            changed_lorebooks.add(key)
    for path in json_files(root, ("presets",)):
        if (key := update_json_file(path, pick_card, write)):
            changed_cards.add(key)
    for directory in ("presets", "cards_gateway"):
        base = root / directory
        if base.is_dir():
            for path in sorted(base.rglob("*.png")):
                if not SKIP_DIRS.intersection(path.relative_to(root).parts[:-1]):
                    if (name := update_png(path, cards, write, found_cards)):
                        changed_cards.add(name)

    for kind, wanted, found in (("Szene", scenes, found_scenes),
                                ("Lorebook", lorebooks, found_lorebooks),
                                ("Karte", cards, found_cards)):
        for key in sorted(set(wanted) - found):
            print(f"WARNUNG: {kind} {key} nicht gefunden")

    bumped = bump(root, "stages_registry.json", "scenes", "id", changed_scenes, write)
    bumped += bump(root, "lorebooks_registry.json", "lorebooks", "name", changed_lorebooks, write)
    bumped += bump(root, "soul_registry.json", "characters", "name", changed_cards, write)
    verb = "geändert" if write else "würden geändert"
    print(f"Szenen {verb}: {len(changed_scenes)}, Lorebooks: {len(changed_lorebooks)}, Karten: {len(changed_cards)}")
    print(f"Registry-Revisionen erhöht: {len(bumped)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
