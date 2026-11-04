#!/usr/bin/env python3
"""Checks a contribution package from the app (ZIP from "Contribute to the hub") and can take it in.

Usage (from the repository root):
    python3 tools/check_submission.py --zip paket.zip                     # check a local package
    python3 tools/check_submission.py --issue-body-env ISSUE_BODY         # find the ZIP in an issue text
    python3 tools/check_submission.py --zip paket.zip --apply --issue 12  # also copy it in + registry entry

`--report FILE` writes the result as Markdown (for the issue comment). Exit code 0: no errors,
1: errors, 2: no package found or not readable. The package is only read, never run: it may come
from anyone. `--apply` writes the card or scene to its gateway folder and adds a registry entry;
afterwards run `validate_content.py --sync-registry` for the list texts and translations.
"""
import argparse
import datetime
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.request
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_content as vc  # noqa: E402  (same folder; its checks follow this repository's rules)

ROOT = vc.ROOT
LICENSES = {'CC0-1.0', 'CC-BY-4.0', 'CC-BY-SA-4.0'}
LICENSE_KEY = 'otakusoul_license'
NSFW_MARK = 'otakusoul_nsfw'
MAX_ZIP_BYTES = 25 * 1024 * 1024        # GitHub's limit for issue attachments
MAX_UNPACKED_BYTES = 40 * 1024 * 1024
MAX_ENTRIES = 20
MAX_PICTURE_BYTES = 8 * 1024 * 1024
CONTENT_PATH = re.compile(r'^(cards_gateway/[A-Za-z0-9_-]{1,80}\.png|stages_gateway/[A-Za-z0-9_-]{1,80}\.json)$')
EXTRA_FILES = {'EINREICHUNG.json', 'README.txt'}
# Traces of the sender's computer: user folders, drives, local files, VRoid Hub models.
LOCAL_TRACES = [
    (re.compile(r'(?i)\b[a-z]:[\\/]'), 'einen Laufwerkspfad'),
    (re.compile(r'(?i)[\\/](users|home)[\\/][^\\/\s]+'), 'einen Benutzerordner'),
    (re.compile(r'(?i)\bfile://'), 'eine lokale Datei'),
    (re.compile(r'^vroid:'), 'ein VRoid-Hub-Modell, das nicht ins Hub darf'),
]
ATTACHMENT = re.compile(
    r'https://github\.com/(?:user-attachments/files/\d+/|[\w.-]+/[\w.-]+/files/\d+/)[^\s)\]>"\'<]+?\.zip',
    re.IGNORECASE,
)

errors: list[str] = []
warnings: list[str] = []
# SHA-256 of the checked ZIP: shows in the comment, so a package swapped after review stands out.
package_sha = ''


def this_repo() -> str:
    """`owner/name` of this repository (Actions sets it; locally from the remote)."""
    if os.environ.get('GITHUB_REPOSITORY'):
        return os.environ['GITHUB_REPOSITORY']
    try:
        url = subprocess.run(['git', 'remote', 'get-url', 'origin'], cwd=ROOT, capture_output=True,
                             text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return 'SnowwhiteOakheart/otakusoul-data'
    return re.sub(r'(\.git)?$', '', url.split('github.com', 1)[-1].lstrip(':/'))


def is_adult_repo() -> bool:
    return this_repo().lower().endswith('-nsfw')


# ---------------------------------------------------------------------------------------------
# Getting the package

def zip_from_issue(body: str) -> bytes | None:
    """The last ZIP attached to the issue text (GitHub attachment addresses only)."""
    urls = ATTACHMENT.findall(body or '')
    if not urls:
        return None
    request = urllib.request.Request(urls[-1], headers={'User-Agent': 'otakusoul-data-check'})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read(MAX_ZIP_BYTES + 1)
    if len(data) > MAX_ZIP_BYTES:
        raise ValueError(f'Paket größer als {MAX_ZIP_BYTES // (1024 * 1024)} MB')
    return data


def read_package(data: bytes) -> dict[str, bytes] | None:
    """The files of the ZIP by name, after the checks that keep a hostile archive harmless."""
    try:
        archive = zipfile.ZipFile(io.BytesIO(data))
    except zipfile.BadZipFile:
        errors.append('Die Datei ist kein ZIP-Archiv.')
        return None
    infos = [i for i in archive.infolist() if not i.is_dir()]
    if len(infos) > MAX_ENTRIES:
        errors.append(f'Zu viele Dateien im Paket ({len(infos)}, höchstens {MAX_ENTRIES}).')
        return None
    if sum(i.file_size for i in infos) > MAX_UNPACKED_BYTES:
        errors.append('Das Paket ist entpackt zu groß.')
        return None
    files = {}
    for info in infos:
        name = info.filename
        if (info.external_attr >> 16) & 0o170000 == 0o120000:
            errors.append(f'`{name}`: symbolische Verknüpfungen sind nicht erlaubt.')
            continue
        if name not in EXTRA_FILES and not CONTENT_PATH.match(name):
            errors.append(f'`{name}`: unerwartete Datei (erlaubt: eine Karte in `cards_gateway/` oder eine '
                          'Geschichte in `stages_gateway/`, dazu `EINREICHUNG.json` und `README.txt`).')
            continue
        files[name] = archive.read(info)
    return files


# ---------------------------------------------------------------------------------------------
# Checks

def local_traces(value, where: str):
    """Errors for strings that point into the sender's computer or to VRoid Hub."""
    if isinstance(value, dict):
        for key, item in value.items():
            local_traces(item, f'{where}.{key}')
    elif isinstance(value, list):
        for i, item in enumerate(value):
            local_traces(item, f'{where}[{i}]')
    elif isinstance(value, str) and not value.startswith(('data:', 'http://', 'https://')):
        for pattern, label in LOCAL_TRACES:
            if pattern.search(value):
                errors.append(f'`{where}`: verweist auf {label} (`{value[:80]}`). Mit einer aktuellen App '
                              'neu exportieren oder den Eintrag entfernen.')
                break


def check_manifest(manifest, files: dict[str, bytes]) -> dict | None:
    if not isinstance(manifest, dict) or manifest.get('schema') != 1 or not isinstance(manifest.get('files'), list):
        errors.append('`EINREICHUNG.json`: unbekanntes Format (schema 1 erwartet).')
        return None
    if manifest.get('kind') not in ('character', 'story'):
        errors.append(f'`EINREICHUNG.json`: unbekannte Art `{manifest.get("kind")}`.')
    if manifest.get('license') not in LICENSES:
        errors.append(f'Lizenz `{manifest.get("license")}` ist nicht erlaubt ({", ".join(sorted(LICENSES))}).')
    author = manifest.get('author')
    if not isinstance(author, str) or not author.strip() or len(author) > 80:
        errors.append('Autor:in fehlt oder ist länger als 80 Zeichen.')
    if not isinstance(manifest.get('adult'), bool):
        errors.append('Altersmarke (`adult`) fehlt.')
    elif manifest['adult'] != is_adult_repo():
        target = 'otakusoul-data-nsfw' if manifest['adult'] else 'otakusoul-data'
        errors.append(f'Falsches Repository: Dieser Beitrag ist als {"ab 18" if manifest["adult"] else "jugendfrei"} '
                      f'markiert und gehört nach `{target}`.')
    listed = {}
    for entry in manifest.get('files') or []:
        path = entry.get('path') if isinstance(entry, dict) else None
        if path not in files:
            errors.append(f'`EINREICHUNG.json` nennt `{path}`, das im Paket fehlt.')
            continue
        data = files[path]
        if entry.get('bytes') != len(data) or entry.get('sha256') != hashlib.sha256(data).hexdigest():
            errors.append(f'`{path}`: Größe oder Prüfsumme passt nicht zu `EINREICHUNG.json`.')
        listed[path] = data
    for path in files:
        if path not in EXTRA_FILES and path not in listed:
            errors.append(f'`{path}` steht nicht in `EINREICHUNG.json`.')
    return manifest


def check_marks(extensions: dict, manifest: dict, where: str):
    license_id = extensions.get(LICENSE_KEY)
    if license_id != manifest.get('license'):
        errors.append(f'`{where}`: Lizenz `{license_id}` passt nicht zu `EINREICHUNG.json` ({manifest.get("license")}).')
    # A missing mark in the adult repository is reported by validate_content's own check.
    if extensions.get(NSFW_MARK) is True and not is_adult_repo():
        errors.append(f'`{where}`: als ab 18 markiert, gehört nach `otakusoul-data-nsfw`.')


def registry_entries(file: str, key: str) -> list[dict]:
    with open(os.path.join(ROOT, file), encoding='utf-8') as f:
        return json.load(f).get(key) or []


def run_repo_checks(check):
    """Runs one of `validate_content`'s checks and takes over its findings (paths shown as given)."""
    vc.errors.clear()
    vc.warnings.clear()
    check()
    errors.extend(vc.errors)
    warnings.extend(vc.warnings)


def check_character(path: str, data: bytes, manifest: dict) -> dict | None:
    if len(data) > MAX_PICTURE_BYTES:
        errors.append(f'`{path}`: Bild größer als {MAX_PICTURE_BYTES // (1024 * 1024)} MB.')
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
        tmp.write(data)
    try:
        card = vc.png_card(tmp.name)
    except (ValueError, json.JSONDecodeError):
        card = None
    finally:
        os.unlink(tmp.name)
    if not isinstance(card, dict):
        errors.append(f'`{path}`: keine Charakterkarte im PNG gefunden.')
        return None
    data_ = card.get('data') or {}
    extensions = data_.get('extensions') or {}
    check_marks(extensions, manifest, path)
    local_traces(data_, 'data')
    name = (data_.get('name') or '').strip()
    if name and any(e.get('name', '').strip().lower() == name.lower() for e in registry_entries('soul_registry.json', 'characters')):
        errors.append(f'Eine Figur „{name}“ gibt es schon im Hub (Aktualisierung? Dann bitte von Hand übernehmen).')
    run_repo_checks(lambda: vc.check_card(os.path.join(ROOT, path), card))
    return card


def check_story(path: str, data: bytes, manifest: dict) -> dict | None:
    try:
        scene = json.loads(data.decode('utf-8'))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        errors.append(f'`{path}`: kein gültiges JSON ({e}).')
        return None
    if not isinstance(scene, dict):
        errors.append(f'`{path}`: keine Szene.')
        return None
    for field in ('title', 'description', 'opening_narration', 'starting_location'):
        if not str(scene.get(field) or '').strip():
            errors.append(f'`{path}`: Feld `{field}` ist leer.')
    stem = os.path.splitext(os.path.basename(path))[0]
    if scene.get('id') != stem:
        warnings.append(f'`{path}`: `id` ({scene.get("id")}) weicht vom Dateinamen ab; bei der Aufnahme wird sie angeglichen.')
    check_marks(scene.get('extensions') or {}, manifest, path)
    local_traces(scene, 'scene')
    known = {e.get('name', '').strip().lower() for e in registry_entries('soul_registry.json', 'characters')}
    known |= {vc.short_name(n) for n in known} | vc.APP_STARTERS
    party = [m if isinstance(m, str) else (m or {}).get('name', '') for m in scene.get('party') or []]
    for member in party:
        if member.lower() not in known and vc.short_name(member) not in known:
            warnings.append(f'Gefährte „{member}“ ist weder im Hub noch in der App; die Figur bitte mit einreichen.')
    books = {e.get('name') for e in registry_entries('lorebooks_registry.json', 'lorebooks')}
    # Party members are checked above (as a warning), so the repository check only sees known names.
    names = {m.lower() for m in party} | known
    run_repo_checks(lambda: vc.check_scene(os.path.join(ROOT, path), scene, names, books))
    if any(e.get('id', '').lower() == stem.lower() for e in registry_entries('stages_registry.json', 'scenes')):
        errors.append(f'Eine Geschichte mit der ID `{stem}` gibt es schon im Hub.')
    return scene


def check_package(files: dict[str, bytes]) -> tuple[dict, str, object] | None:
    """Checks everything; returns (manifest, content path, card or scene) when it got that far."""
    if 'EINREICHUNG.json' not in files:
        errors.append('`EINREICHUNG.json` fehlt – ist das ein Paket aus der App („Zum Hub beisteuern“)?')
        return None
    try:
        manifest = json.loads(files['EINREICHUNG.json'].decode('utf-8'))
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        errors.append(f'`EINREICHUNG.json`: kein gültiges JSON ({e}).')
        return None
    manifest = check_manifest(manifest, files)
    if manifest is None:
        return None
    content = [p for p in files if p not in EXTRA_FILES]
    wanted = 'cards_gateway/' if manifest.get('kind') == 'character' else 'stages_gateway/'
    content = [p for p in content if p.startswith(wanted)]
    if len(content) != 1:
        errors.append(f'Das Paket braucht genau eine Datei in `{wanted}` (gefunden: {len(content)}).')
        return None
    path = content[0]
    target = os.path.join(ROOT, normalized_path(path))
    if os.path.exists(target):
        errors.append(f'`{normalized_path(path)}` gibt es schon im Repository.')
    check = check_character if manifest['kind'] == 'character' else check_story
    item = check(path, files[path], manifest)
    return (manifest, path, item) if item is not None else None


def normalized_path(path: str) -> str:
    """Repository convention: lower-case file names."""
    folder, name = path.split('/', 1)
    return f'{folder}/{name.lower()}'


# ---------------------------------------------------------------------------------------------
# Taking it in

def apply(manifest: dict, path: str, item, files: dict[str, bytes], issue: int | None) -> str:
    """Writes the file into the repository and adds the registry entry; returns the new path."""
    target = normalized_path(path)
    stem = os.path.splitext(os.path.basename(target))[0]
    if stem == 'beitrag' and issue:
        target = target.replace('beitrag', f'beitrag_{issue}')
        stem = f'beitrag_{issue}'
    url = f'https://raw.githubusercontent.com/{this_repo()}/main/{target}'
    today = datetime.date.today().isoformat()
    os.makedirs(os.path.join(ROOT, os.path.dirname(target)), exist_ok=True)
    if manifest['kind'] == 'character':
        with open(os.path.join(ROOT, target), 'wb') as f:
            f.write(files[path])
        entry = {'name': item['data']['name'].strip(), 'author': manifest['author'].strip(),
                 'download_url': url, 'revision': 1, 'updated': today}
        registry, key = 'soul_registry.json', 'characters'
    else:
        item['id'] = stem
        with open(os.path.join(ROOT, target), 'w', encoding='utf-8') as f:
            f.write(json.dumps(item, ensure_ascii=False, indent=2) + '\n')
        entry = {'id': stem, 'title': item.get('title', ''), 'description': item.get('description', ''),
                 'starting_location': item.get('starting_location', ''), 'author': manifest['author'].strip(),
                 'download_url': url, 'revision': 1, 'updated': today}
        registry, key = 'stages_registry.json', 'scenes'
    registry_path = os.path.join(ROOT, registry)
    with open(registry_path, encoding='utf-8') as f:
        content = json.load(f)
    content.setdefault(key, []).append(entry)
    with open(registry_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False, indent=2) + '\n')
    return target


# ---------------------------------------------------------------------------------------------

def report(manifest: dict | None, applied: str | None) -> str:
    lines = ['<!-- otakusoul-pruefung -->']
    if errors:
        lines.append(f'### ❌ Prüfung: {len(errors)} Fehler / check failed')
    else:
        lines.append('### ✅ Prüfung bestanden / check passed')
    if manifest:
        lines.append('')
        lines.append(f'**{manifest.get("kind")}** „{manifest.get("title")}“ von {manifest.get("author")} · '
                     f'{manifest.get("license")} · {"ab 18" if manifest.get("adult") else "jugendfrei"} · '
                     f'App {manifest.get("app_version", "?")}')
    if package_sha:
        lines.append(f'Paket SHA-256: `{package_sha}`')
    if errors:
        lines += ['', '**Fehler** (verhindern die Aufnahme):'] + [f'- {e}' for e in errors]
    if warnings:
        lines += ['', f'<details><summary>{len(warnings)} Hinweise (verhindern nichts)</summary>', '']
        lines += [f'- {w}' for w in warnings] + ['', '</details>']
    lines.append('')
    if applied:
        lines.append(f'Übernommen als `{applied}`.')
    elif errors:
        lines.append('Bitte die Fehler beheben, ein neues Paket aus der App speichern und das Issue mit dem neuen '
                     'Anhang bearbeiten – die Prüfung läuft dann erneut.')
    else:
        lines.append('Die Inhalte (Rechte, Altersmarke, Ton) prüfen wir noch von Hand. Mit dem Label `aufnehmen` '
                     'entsteht ein Pull Request.')
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--zip', help='Pfad zum ZIP-Paket')
    source.add_argument('--issue-body-env', help='Umgebungsvariable mit dem Issue-Text (ZIP-Anhang darin)')
    parser.add_argument('--report', help='Ergebnis als Markdown in diese Datei')
    parser.add_argument('--apply', action='store_true', help='bei Erfolg Datei und Registry-Eintrag übernehmen')
    parser.add_argument('--issue', type=int, help='Nummer des Issues (für eindeutige Dateinamen)')
    args = parser.parse_args()

    def finish(code: int, manifest=None, applied=None):
        text = report(manifest, applied)
        if args.report:
            with open(args.report, 'w', encoding='utf-8') as f:
                f.write(text)
        sys.stdout.reconfigure(encoding='utf-8')
        print(text)
        sys.exit(code)

    try:
        if args.zip:
            with open(args.zip, 'rb') as f:
                data = f.read(MAX_ZIP_BYTES + 1)
            if len(data) > MAX_ZIP_BYTES:
                raise ValueError('Paket zu groß')
        else:
            data = zip_from_issue(os.environ.get(args.issue_body_env, ''))
    except (OSError, ValueError) as e:
        errors.append(f'Das Paket ließ sich nicht laden ({e}).')
        finish(2)
    if data is None:
        errors.append('Kein ZIP-Anhang gefunden. Bitte das Paket aus der App ins Issue ziehen.')
        finish(2)
    global package_sha
    package_sha = hashlib.sha256(data).hexdigest()
    # Anything a hostile or broken package trips (encrypted members, wrong types in the
    # manifest or card) still ends in a report, so the issue always gets an answer.
    try:
        files = read_package(data)
        result = check_package(files) if files is not None else None
    except Exception as e:  # noqa: BLE001
        errors.append(f'Das Paket ließ sich nicht lesen ({type(e).__name__}: {e}).')
        finish(1)
    manifest = result[0] if result else None
    if errors or not result:
        finish(1, manifest)
    applied = apply(*result, files, args.issue) if args.apply else None
    finish(0, manifest, applied)


if __name__ == '__main__':
    main()
