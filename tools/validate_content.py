#!/usr/bin/env python3
"""Checks the structure of the content repository (cards, scenes, lorebooks, registries, model catalogue).

Usage (from the repository root):
    python3 tools/validate_content.py                  # check only, exit code 1 on errors
    python3 tools/validate_content.py --sync-registry  # also copy list texts from the files into the registries

Errors break the app or the hub (missing files, unknown party members, files that differ only in
case, …); warnings are worth a look (missing translations, fewer than two greetings).
`--sync-registry` sets title/name, description and starting location of every scene and lorebook
entry from its file, with the file's translations under `translations.<lang>`; the registry name of a
lorebook and the id of a scene stay as they are (they are the keys for updates).
"""
import argparse
import hashlib
import base64
import collections
import json
import os
import struct
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = {'de', 'en', 'ru', 'ja'}
EMOTIONS = {'neutral', 'happy', 'relaxed', 'surprised', 'angry', 'sad'}
CARD_TEXT = ['description', 'personality', 'scenario', 'first_mes', 'mes_example', 'system_prompt',
             'post_history_instructions', 'creator_notes']
SCENE_TEXT = ['title', 'description', 'world_context', 'starting_location', 'time_of_day',
              'opening_narration', 'first_message', 'gm_tone', 'narrator_style']
TRIGGERS = {'keyword', 'regex', 'always_on', 'tension'}
OBSOLETE_SCENE_FIELDS = {'conversation_method'}

errors: list[str] = []
warnings: list[str] = []


def rel(path: str) -> str:
    return os.path.relpath(path, ROOT)


def load_json(path: str):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        errors.append(f'{rel(path)}: kein gültiges JSON ({e})')
        return None


def png_card(path: str):
    """The Character Card V2 in a PNG's `chara` text chunk, or None."""
    with open(path, 'rb') as f:
        data = f.read()
    if not data.startswith(b'\x89PNG\r\n\x1a\n'):
        return None
    i = 8
    while i + 8 <= len(data):
        length = struct.unpack('>I', data[i:i + 4])[0]
        kind, body = data[i + 4:i + 8], data[i + 8:i + 8 + length]
        if kind == b'tEXt' and body.startswith(b'chara\0'):
            return json.loads(base64.b64decode(body[6:]))
        i += 12 + length
    return None


def repo_file(url: str) -> str:
    return os.path.join(ROOT, urllib.parse.unquote(url.split('/main/', 1)[-1]))


def short_name(name: str) -> str:
    return name.split(' (')[0].strip().lower()


# ---------------------------------------------------------------------------------------------
# Character cards

def check_card(path: str, card: dict):
    data = card.get('data') or {}
    where = rel(path)
    if card.get('spec') != 'chara_card_v2' or card.get('spec_version') != '2.0':
        errors.append(f'{where}: spec/spec_version fehlen oder falsch')
    for key in ('name', 'description', 'first_mes'):
        if not data.get(key):
            errors.append(f'{where}: Feld {key} leer')
    ext = data.get('extensions') or {}
    legacy = [k for k in ext if k.startswith('sow_')]
    if legacy:
        warnings.append(f'{where}: alte Schlüssel {legacy} (custom_* verwenden)')
    i18n = ext.get('otakusoul_i18n')
    if not i18n:
        warnings.append(f'{where}: keine Übersetzungen (otakusoul_i18n)')
    else:
        source = i18n.get('source_language')
        translations = i18n.get('translations') or {}
        if set(translations) != LANGS - {source}:
            warnings.append(f'{where}: Übersetzungen {sorted(translations)} bei Ausgangssprache {source}')
        for lang, t in translations.items():
            missing = [k for k in CARD_TEXT if data.get(k) and not t.get(k)]
            if missing:
                warnings.append(f'{where} [{lang}]: nicht übersetzt {missing}')
            greetings = t.get('alternate_greetings')
            if greetings is not None and len(greetings) != len(data.get('alternate_greetings') or []):
                warnings.append(f'{where} [{lang}]: Anzahl alternate_greetings weicht ab')
    if len(data.get('alternate_greetings') or []) < 2:
        warnings.append(f'{where}: weniger als zwei alternative Begrüßungen')
    expressions = ext.get('expressions')
    if isinstance(expressions, dict):
        missing = EMOTIONS - set(expressions)
        if missing:
            warnings.append(f'{where}: Emotionsbilder fehlen {sorted(missing)}')
        for key, value in expressions.items():
            if isinstance(value, str) and not value.startswith(('http://', 'https://', 'data:')):
                if not os.path.exists(os.path.join(os.path.dirname(path), value)):
                    errors.append(f'{where}: Emotionsbild {key} fehlt ({value})')


def collect_cards() -> dict[str, tuple[str, dict]]:
    cards = {}
    for folder, _, files in os.walk(ROOT):
        if '/.git' in folder or '/venv' in folder or '/.venv' in folder or '/expressions' in folder:
            continue
        for name in files:
            path = os.path.join(folder, name)
            card = None
            if name.endswith('.png'):
                card = png_card(path)
            elif name.endswith('.json') and '/presets/' in path and '/scenes/' not in path and '/lorebooks/' not in path:
                content = load_json(path)
                card = content if isinstance(content, dict) and content.get('spec') == 'chara_card_v2' else None
            if card:
                cards[path] = (path, card)
                check_card(path, card)
    # A preset JSON and its PNG carry the same card.
    for path, (_, card) in cards.items():
        if path.endswith('.json'):
            png = path[:-5] + '.png'
            if png in cards and cards[png][1] != card:
                errors.append(f'{rel(path)}: JSON und PNG-Payload unterscheiden sich')
    return cards


# ---------------------------------------------------------------------------------------------
# Registries, scenes, lorebooks

def check_gateway_files(registry: list[dict]):
    folder = os.path.join(ROOT, 'cards_gateway')
    files = [f for f in os.listdir(folder) if not f.startswith('.')]
    by_lower = collections.defaultdict(list)
    for name in files:
        by_lower[name.lower()].append(name)
    for names in by_lower.values():
        if len(names) > 1:
            errors.append(f'cards_gateway: Namen unterscheiden sich nur in der Groß-/Kleinschreibung {names} (Windows/macOS)')
    used = {os.path.basename(repo_file(e['download_url'])) for e in registry}
    for name in files:
        if name not in used:
            warnings.append(f'cards_gateway/{name}: steht in keiner Registry')


def check_registry(file: str, key: str, required: list[str]) -> list[dict]:
    content = load_json(os.path.join(ROOT, file))
    if not content:
        return []
    entries = content.get(key) or []
    seen = set()
    for e in entries:
        label = e.get('id') or e.get('name') or e.get('title')
        for field in required + ['download_url', 'revision', 'updated']:
            if field not in e:
                errors.append(f'{file}: {label}: Feld {field} fehlt')
        if label in seen:
            errors.append(f'{file}: {label} doppelt')
        seen.add(label)
        if not os.path.exists(repo_file(e.get('download_url', ''))):
            errors.append(f'{file}: {label}: Datei fehlt ({e.get("download_url")})')
    return entries


def check_scene(path: str, scene: dict, names: set[str], lorebooks: set[str]):
    where = rel(path)
    for field in OBSOLETE_SCENE_FIELDS & set(scene):
        warnings.append(f'{where}: veraltetes Feld {field}')
    if scene.get('persona') == 'None':
        errors.append(f'{where}: persona "None" (leer lassen für die aktive Persona)')
    for member in scene.get('party') or []:
        name = member if isinstance(member, str) else (member or {}).get('name', '')
        if name.lower() not in names and short_name(name) not in names:
            errors.append(f'{where}: Mitspieler „{name}“ hat keine Karte')
    for book in scene.get('lorebook') or []:
        if book not in lorebooks:
            errors.append(f'{where}: Lorebook „{book}“ unbekannt')
    ext = scene.get('extensions') or {}
    for asset in (ext.get('otakusoul_assets') or {}).get('backgrounds') or []:
        if not os.path.exists(os.path.join(ROOT, asset.get('path', ''))):
            errors.append(f'{where}: Hintergrund fehlt ({asset.get("path")})')
    i18n = ext.get('otakusoul_i18n')
    if not i18n:
        warnings.append(f'{where}: keine Übersetzungen')
    else:
        for lang in LANGS - {i18n.get('source_language')}:
            t = (i18n.get('translations') or {}).get(lang) or {}
            missing = [k for k in SCENE_TEXT if scene.get(k) and not t.get(k)]
            if missing:
                warnings.append(f'{where} [{lang}]: nicht übersetzt {missing}')
    story = ext.get('otakusoul_story')
    if not story:
        warnings.append(f'{where}: keine Story-Daten (otakusoul_story)')
    else:
        for lang in sorted(LANGS):
            if len((story.get('choices') or {}).get(lang) or []) != 3:
                warnings.append(f'{where} [{lang}]: nicht genau drei Startvorschläge')


def check_lorebook(path: str, book: dict):
    where = rel(path)
    uids = [e.get('uid') for e in book.get('entries') or []]
    if None in uids or len(set(uids)) != len(uids):
        errors.append(f'{where}: uid fehlt oder doppelt')
    for entry in book.get('entries') or []:
        label = f'{where}: {entry.get("name")}'
        if entry.get('trigger_type') not in TRIGGERS:
            errors.append(f'{label}: trigger_type {entry.get("trigger_type")!r} (erlaubt: {sorted(TRIGGERS)})')
        if entry.get('trigger_type') == 'keyword' and not entry.get('key'):
            errors.append(f'{label}: keyword ohne Schlüsselwörter')
        for req in entry.get('chain_requires') or []:
            if str(req) not in {str(u) for u in uids}:
                errors.append(f'{label}: chain_requires {req} zeigt auf keinen Eintrag')
        legacy = {'n_depth', 'depends_on', 'sticky', 'cooldown', 'delay', 'semantic_trigger'} & set(entry)
        if legacy:
            warnings.append(f'{label}: alte Felder {sorted(legacy)}')


def localized(content: dict, fields: list[str]) -> dict:
    i18n = (content.get('extensions') or {}).get('otakusoul_i18n') or {}
    out = {}
    for lang, t in (i18n.get('translations') or {}).items():
        texts = {f: t[f] for f in fields if isinstance(t.get(f), str) and t[f]}
        if texts:
            out[lang] = texts
    return out


def sync_registry(file: str, key: str, fields: dict[str, str]):
    """Copies list texts (`fields`: registry field → file field) and their translations."""
    path = os.path.join(ROOT, file)
    content = load_json(path)
    changed = 0
    for e in content.get(key) or []:
        source = load_json(repo_file(e['download_url']))
        if not source:
            continue
        before = json.dumps(e, sort_keys=True)
        for reg_field, file_field in fields.items():
            if isinstance(source.get(file_field), str):
                e[reg_field] = source[file_field]
        texts = localized(source, list(fields.values()))
        if texts:
            e['translations'] = {lang: {reg: t[f] for reg, f in fields.items() if f in t} for lang, t in sorted(texts.items())}
        if json.dumps(e, sort_keys=True) != before:
            changed += 1
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False, indent=2) + '\n')
    print(f'{file}: {changed} Einträge abgeglichen')


def check_collections(souls: list[dict], books: list[dict], scenes: list[dict]) -> int:
    """Collections group lorebooks, scenes and characters of one story; every reference must exist."""
    content = load_json(os.path.join(ROOT, 'collections_registry.json'))
    if not content:
        return 0
    soul_names = {e.get('name') for e in souls}
    book_names = {e.get('name') for e in books}
    scene_ids = {e.get('id'): e for e in scenes}
    seen = set()
    entries = content.get('collections') or []
    for c in entries:
        label = f'collections_registry.json: {c.get("id")}'
        for field in ('id', 'title', 'author', 'description', 'cover_url', 'revision', 'updated'):
            if field not in c:
                errors.append(f'{label}: Feld {field} fehlt')
        if c.get('id') in seen:
            errors.append(f'{label} doppelt')
        seen.add(c.get('id'))
        if c.get('cover_url') and not os.path.exists(repo_file(c['cover_url'])):
            errors.append(f'{label}: Titelbild fehlt ({c["cover_url"]})')
        for name in c.get('lorebooks') or []:
            if name not in book_names:
                errors.append(f'{label}: Lorebook {name!r} steht nicht in lorebooks_registry.json')
        for name in c.get('characters') or []:
            if name not in soul_names:
                errors.append(f'{label}: Charakter {name!r} steht nicht in soul_registry.json')
        listed = {n.lower() for n in c.get('characters') or []} | {short_name(n) for n in c.get('characters') or []}
        for sid in c.get('scenes') or []:
            entry = scene_ids.get(sid)
            if not entry:
                errors.append(f'{label}: Szene {sid!r} steht nicht in stages_registry.json')
                continue
            scene = load_json(repo_file(entry['download_url'])) or {}
            for member in scene.get('party') or []:
                if member.lower() not in listed and short_name(member) not in listed:
                    warnings.append(f'{label}: {member} spielt in {sid} mit, fehlt aber in characters')
    return len(entries)


OPEN_LICENSES = {'apache-2.0', 'mit', 'bsd-2-clause', 'bsd-3-clause'}


def check_models():
    """recommended_models.json: what the app's model catalogue needs (model_catalog.rs)."""
    content = load_json(os.path.join(ROOT, 'recommended_models.json'))
    if not content:
        return 0
    if not content.get('version'):
        errors.append('recommended_models.json: version fehlt')
    seen = set()
    for m in content.get('models') or []:
        label = f'recommended_models.json: {m.get("id")}'
        for field in ('id', 'name', 'hf_id', 'file', 'size_bytes', 'sha256', 'license', 'quantization', 'runtime', 'vram_mb'):
            if not m.get(field):
                errors.append(f'{label}: Feld {field} fehlt')
        if m.get('id') in seen:
            errors.append(f'{label}: doppelt')
        seen.add(m.get('id'))
        sha = str(m.get('sha256', ''))
        if len(sha) != 64 or any(c not in '0123456789abcdef' for c in sha.lower()):
            errors.append(f'{label}: sha256 ungültig')
        repo = str(m.get('hf_id', ''))
        if repo.count('/') != 1 or '..' in repo or not str(m.get('file', '')).lower().endswith('.gguf') or '/' in str(m.get('file', '')):
            errors.append(f'{label}: hf_id oder file ungültig')
        if m.get('runtime') not in ('standard', 'prism'):
            errors.append(f'{label}: runtime {m.get("runtime")!r} unbekannt')
        if set((m.get('description') or {})) != LANGS:
            warnings.append(f'{label}: description nicht in {sorted(LANGS)}')
        if str(m.get('license', '')).lower() not in OPEN_LICENSES and set((m.get('license_note') or {})) != LANGS:
            errors.append(f'{label}: Lizenz {m.get("license")!r} ist nicht frei – license_note in {sorted(LANGS)} nötig')
        url = m.get('license_url')
        if url and not str(url).startswith('https://'):
            errors.append(f'{label}: license_url muss https sein')
    return len(content.get('models') or [])


def check_puppets():
    """inochi2d_registry.json: Inochi2D puppets the app offers to download (inochi2d.rs)."""
    content = load_json(os.path.join(ROOT, 'inochi2d_registry.json'))
    if not content:
        return 0
    if not content.get('version'):
        errors.append('inochi2d_registry.json: version fehlt')
    seen = set()
    for p in content.get('puppets') or []:
        label = f'inochi2d_registry.json: {p.get("id")}'
        for field in ('id', 'name', 'author', 'license', 'url', 'sha256', 'size_bytes'):
            if not p.get(field):
                errors.append(f'{label}: Feld {field} fehlt')
        pid = str(p.get('id', ''))
        if pid in seen:
            errors.append(f'{label}: doppelt')
        seen.add(pid)
        if '/' in pid or '\\' in pid or pid.startswith('.') or not pid.lower().endswith(('.inp', '.inx')):
            errors.append(f'{label}: id muss ein Dateiname .inp/.inx sein')
        sha = str(p.get('sha256', ''))
        if len(sha) != 64 or any(c not in '0123456789abcdef' for c in sha):
            errors.append(f'{label}: sha256 ungültig (64 Kleinbuchstaben-Hex)')
        for key in ('url', 'license_url'):
            if p.get(key) and not str(p[key]).startswith('https://'):
                errors.append(f'{label}: {key} muss https sein')
        if set((p.get('description') or {})) != LANGS:
            warnings.append(f'{label}: description nicht in {sorted(LANGS)}')
    return len(content.get('puppets') or [])


def repo_blob_sha(rel):
    """SHA-256 of a file as committed (what GitHub serves), else of the working copy."""
    import subprocess
    try:
        data = subprocess.run(['git', '-C', ROOT, 'cat-file', '-p', f'HEAD:{rel}'], capture_output=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        data = open(os.path.join(ROOT, *rel.split('/')), 'rb').read()
    return hashlib.sha256(data).hexdigest(), len(data)


def check_avatars():
    """avatars_registry.json: VRM and Live2D models the hub offers (avatar_hub.rs)."""
    content = load_json(os.path.join(ROOT, 'avatars_registry.json'))
    if not content:
        return 0
    if not content.get('version'):
        errors.append('avatars_registry.json: version fehlt')
    prefix = 'https://raw.githubusercontent.com/SnowwhiteOakheart/otakusoul-data/main/'
    seen = set()
    for a in content.get('avatars') or []:
        label = f'avatars_registry.json: {a.get("id")}'
        for field in ('id', 'kind', 'name', 'author', 'license'):
            if not a.get(field):
                errors.append(f'{label}: Feld {field} fehlt')
        if a.get('id') in seen:
            errors.append(f'{label}: doppelt')
        seen.add(a.get('id'))
        if a.get('kind') not in ('vrm', 'live2d'):
            errors.append(f'{label}: kind muss vrm oder live2d sein')
        if set((a.get('description') or {})) != LANGS:
            warnings.append(f'{label}: description nicht in {sorted(LANGS)}')
        files = a.get('files') or []
        if not files:
            if not str(a.get('page_url', '')).startswith('https://'):
                errors.append(f'{label}: ohne Dateien ist page_url (https) nötig')
            continue
        if a.get('entry') not in [f.get('path') for f in files]:
            errors.append(f'{label}: entry ist keine der Dateien')
        for f in files:
            path = str(f.get('path', ''))
            if not path or path.startswith('/') or '\\' in path or '..' in path.split('/'):
                errors.append(f'{label}/{path}: unsicherer Pfad')
            url = str(f.get('url', ''))
            if not url.startswith('https://'):
                errors.append(f'{label}/{path}: url muss https sein')
            sha = str(f.get('sha256', ''))
            if len(sha) != 64 or any(c not in '0123456789abcdef' for c in sha):
                errors.append(f'{label}/{path}: sha256 ungültig')
            if url.startswith(prefix):
                rel = urllib.parse.unquote(url[len(prefix):])
                if not os.path.isfile(os.path.join(ROOT, *rel.split('/'))):
                    errors.append(f'{label}/{path}: Datei {rel} fehlt im Repository')
                else:
                    digest, size = repo_blob_sha(rel)
                    if digest != sha or size != f.get('size_bytes'):
                        errors.append(f'{label}/{path}: sha256 oder size_bytes passt nicht zur Datei')
    return len(content.get('avatars') or [])


def check_motion_packs():
    """motion_packs_registry.json: motion sets (VRMA) the app offers to download (motion_packs.rs)."""
    content = load_json(os.path.join(ROOT, 'motion_packs_registry.json'))
    if not content:
        return 0
    if not content.get('version'):
        errors.append('motion_packs_registry.json: version fehlt')
    roles = {'idle', 'greeting', 'nod', 'happy', 'sad', 'angry', 'surprised', 'thinking', 'walk', 'sit',
             'talk', 'dance', 'fall', 'sleep', 'jump', 'land', 'yawn'}
    prefix = 'https://raw.githubusercontent.com/SnowwhiteOakheart/otakusoul-data/main/'
    count = 0
    for pack in content.get('packs') or []:
        label = f'motion_packs_registry.json: {pack.get("id")}'
        for field in ('id', 'name', 'author', 'license', 'files'):
            if not pack.get(field):
                errors.append(f'{label}: Feld {field} fehlt')
        if set((pack.get('description') or {})) != LANGS:
            warnings.append(f'{label}: description nicht in {sorted(LANGS)}')
        for f in pack.get('files') or []:
            count += 1
            flabel = f'{label}/{f.get("file")}'
            name = str(f.get('file', ''))
            if '/' in name or '\\' in name or name.startswith('.') or not name.lower().endswith('.vrma'):
                errors.append(f'{flabel}: file muss ein Dateiname .vrma sein')
            if f.get('role', '') and f['role'] not in roles:
                errors.append(f'{flabel}: unbekannte Rolle {f["role"]!r}')
            url = str(f.get('url', ''))
            if not url.startswith('https://'):
                errors.append(f'{flabel}: url muss https sein')
            sha = str(f.get('sha256', ''))
            if len(sha) != 64 or any(c not in '0123456789abcdef' for c in sha):
                errors.append(f'{flabel}: sha256 ungültig (64 Kleinbuchstaben-Hex)')
            # Files in this repository: they must exist and match their checksum and size.
            if url.startswith(prefix):
                local = os.path.join(ROOT, *url[len(prefix):].split('/'))
                if not os.path.isfile(local):
                    errors.append(f'{flabel}: Datei {url[len(prefix):]} fehlt im Repository')
                else:
                    data = open(local, 'rb').read()
                    if hashlib.sha256(data).hexdigest() != sha:
                        errors.append(f'{flabel}: sha256 passt nicht zur Datei')
                    if len(data) != f.get('size_bytes'):
                        errors.append(f'{flabel}: size_bytes passt nicht zur Datei')
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--sync-registry', action='store_true', help='Listentexte aus den Dateien in die Registries übernehmen')
    args = parser.parse_args()

    if args.sync_registry:
        # The lorebook name is its update key and stays; only its translations are taken over.
        sync_registry('stages_registry.json', 'scenes', {'title': 'title', 'description': 'description', 'starting_location': 'starting_location'})
        sync_registry('lorebooks_registry.json', 'lorebooks', {'description': 'description'})
        books = load_json(os.path.join(ROOT, 'lorebooks_registry.json'))
        for e in books['lorebooks']:
            source = load_json(repo_file(e['download_url']))
            for lang, t in localized(source, ['name']).items():
                e.setdefault('translations', {}).setdefault(lang, {})['name'] = t['name']
        with open(os.path.join(ROOT, 'lorebooks_registry.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(books, ensure_ascii=False, indent=2) + '\n')

    cards = collect_cards()
    names = set()
    for _, card in cards.values():
        name = (card.get('data') or {}).get('name', '')
        names.update({name.lower(), short_name(name)})

    souls = check_registry('soul_registry.json', 'characters', ['name', 'author'])
    check_gateway_files(souls)
    books = check_registry('lorebooks_registry.json', 'lorebooks', ['name', 'author', 'description', 'entry_count'])
    scenes = check_registry('stages_registry.json', 'scenes', ['id', 'title', 'author', 'description', 'starting_location'])

    lorebook_names = set()
    for e in books:
        book = load_json(repo_file(e['download_url']))
        if book:
            lorebook_names.add(book.get('name'))
            check_lorebook(repo_file(e['download_url']), book)
            if e.get('entry_count') != len(book.get('entries') or []):
                errors.append(f'lorebooks_registry.json: {e["name"]}: entry_count {e.get("entry_count")} ≠ {len(book.get("entries") or [])}')
            if e.get('description') != book.get('description'):
                warnings.append(f'lorebooks_registry.json: {e["name"]}: Beschreibung weicht von der Datei ab (--sync-registry)')
    for folder in ('presets',):
        for dirpath, _, files in os.walk(os.path.join(ROOT, folder)):
            if dirpath.endswith('/lorebooks'):
                for name in files:
                    if name.endswith('.json'):
                        book = load_json(os.path.join(dirpath, name))
                        if book:
                            lorebook_names.add(book.get('name'))
                            check_lorebook(os.path.join(dirpath, name), book)
    for e in scenes:
        scene = load_json(repo_file(e['download_url']))
        if scene:
            check_scene(repo_file(e['download_url']), scene, names, lorebook_names)
            for field in ('title', 'description', 'starting_location'):
                if e.get(field) != scene.get(field):
                    warnings.append(f'stages_registry.json: {e.get("id")}: {field} weicht von der Datei ab (--sync-registry)')
    for dirpath, _, files in os.walk(os.path.join(ROOT, 'presets')):
        if dirpath.endswith('/scenes'):
            for name in files:
                if name.endswith('.json'):
                    scene = load_json(os.path.join(dirpath, name))
                    if scene:
                        check_scene(os.path.join(dirpath, name), scene, names, lorebook_names)

    collections = check_collections(souls, books, scenes)
    models = check_models()
    puppets = check_puppets()
    motions = check_motion_packs()
    avatars = check_avatars()

    for line in warnings:
        print(f'Warnung: {line}')
    for line in errors:
        print(f'FEHLER:  {line}')
    print(f'{len(cards)} Karten, {len(books)} Lorebooks, {len(scenes)} Szenen, {collections} Sammlungen, {models} Modelle, {puppets} Puppen, {avatars} Avatare, {motions} Bewegungen geprüft: '
          f'{len(errors)} Fehler, {len(warnings)} Warnungen')
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
