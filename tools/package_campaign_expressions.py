"""Normalisiert und prüft ein Emotionspaket; importiert nichts in die App."""
import argparse
import base64
import copy
import hashlib
import json
import struct
import subprocess
import zlib
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://raw.githubusercontent.com/SnowwhiteOakheart/otakusoul-data/main/'
MOODS = ('neutral', 'happy', 'relaxed', 'surprised', 'angry', 'sad')
CAST = {
    'dungeon-meshi': ['laios_touden', 'marcille_donato', 'chilchuck_tims', 'senshi'],
    'steins-gate': ['okabe_rintarou', 'mayuri_shiina', 'itaru_hashida', 'suzuha_amane'],
    'lycoris-recoil': ['chisato_nishikigi', 'takina_inoue', 'mizuki_nakahara', 'kurumi'],
    'sword-art-online': ['kirito_kazuto', 'asuna_yuuki', 'klein_ryoutarou', 'lisbeth_rika'],
}

def read_card(path):
    raw = path.read_bytes()
    pos = 8
    card = None
    while pos < len(raw):
        length = struct.unpack('>I', raw[pos:pos + 4])[0]
        kind = raw[pos + 4:pos + 8]
        body = raw[pos + 8:pos + 8 + length]
        assert zlib.crc32(kind + body) & 0xffffffff == struct.unpack('>I', raw[pos + 8 + length:pos + 12 + length])[0]
        if kind == b'tEXt' and body.startswith(b'chara\0'):
            card = json.loads(base64.b64decode(body.split(b'\0', 1)[1]))
        pos += length + 12
    return card

def embed(path, card):
    raw = path.read_bytes()
    pos = 8
    chunks = []
    while pos < len(raw):
        length = struct.unpack('>I', raw[pos:pos + 4])[0]
        kind = raw[pos + 4:pos + 8]
        body = raw[pos + 8:pos + 8 + length]
        chunk = raw[pos:pos + length + 12]
        pos += length + 12
        if kind == b'tEXt' and body.startswith(b'chara\0'):
            continue
        if kind == b'IEND':
            payload = b'chara\0' + base64.b64encode(json.dumps(card, ensure_ascii=False).encode())
            chunks.append(struct.pack('>I', len(payload)) + b'tEXt' + payload + struct.pack('>I', zlib.crc32(b'tEXt' + payload) & 0xffffffff))
        chunks.append(chunk)
    path.write_bytes(raw[:8] + b''.join(chunks))

def complete(group, slug):
    p = ROOT / 'presets' / group / f'{slug}.json'
    card = json.loads(p.read_text())
    expressions = card['data']['extensions'].get('expressions', {})
    return set(expressions) == set(MOODS) and all((p.parent / expressions[mood]).is_file() for mood in MOODS)

def roadmap(current=None):
    def published(group, slug):
        if current == (group, slug):
            return complete(group, slug)
        tracked = subprocess.check_output(['git', 'ls-files', '--', f'presets/{group}/expressions/{slug}/neutral.webp'], cwd=ROOT)
        return bool(tracked.strip()) and complete(group, slug)
    total = sum(published(g, slug) for g, cast in CAST.items() for slug in cast)
    rows = ['### Kampagnen-Expressions – Fortschritt', '',
            f'{total}/16 Figuren vollständig; {total * 6}/96 Emotionsbilder fertig, {(16-total) * 6} noch offen.', '']
    for group, cast in CAST.items():
        for slug in cast:
            card = json.loads((ROOT / 'presets' / group / f'{slug}.json').read_text())
            done = published(group, slug)
            rows.append(f'- [{"x" if done else " "}] **{card["data"]["name"]}** ({group}): ' + ('sechs Expressions geprüft und in Preset- und Hub-Karte eingebunden.' if done else 'sechs Expressions fehlen.'))
    text = (ROOT / 'ROADMAP.md').read_text()
    old = '- [ ] Für die 16 Kampagnenfiguren je sechs Expressions ergänzen (96 Bilder insgesamt); die vorhandenen Avatare allein decken den allgemeinen Expressions-Qualitätsstandard noch nicht ab.'
    new = '- [' + ('x' if total == 16 else ' ') + '] Kampagnen-Expressions: ' + f'{total}/16 Figuren und {total * 6}/96 Bilder fertig (Einzelstand unten).'
    if old in text:
        text = text.replace(old, new)
    else:
        text = '\n'.join(new if line.startswith('- [') and 'Kampagnen-Expressions:' in line else line for line in text.split('\n'))
    marker = '<!-- campaign-expressions:start -->'
    end = '<!-- campaign-expressions:end -->'
    block = marker + '\n' + '\n'.join(rows) + '\n' + end
    if marker in text:
        begin = text.index(marker)
        finish = text.index(end, begin) + len(end)
        text = text[:begin] + block + text[finish:]
    else:
        text += '\n\n' + block + '\n'
    (ROOT / 'ROADMAP.md').write_text(text)

def package(group, slug, manifest):
    package = ROOT / 'presets' / group
    path = package / f'{slug}.json'
    card = json.loads(path.read_text())
    original = copy.deepcopy(card)
    records = json.loads(Path(manifest).read_text())
    assert {r['mood'] for r in records} == set(MOODS)
    directory = package / 'expressions' / slug
    directory.mkdir(parents=True, exist_ok=True)
    for record in records:
        target = directory / (record['mood'] + '.webp')
        assert not target.exists(), f'Bestehendes Bild: {target}'
        with Image.open(record['path']) as image:
            ImageOps.fit(image.convert('RGB'), (640, 800), centering=(0.5, 0.35)).save(target, quality=92)
    (directory / 'prompts.json').write_text(json.dumps({
        'tool': 'image_gen (eingebaut)', 'reference': f'../../{slug}.png',
        'prompts': {r['mood']: r['prompt'] for r in records}
    }, ensure_ascii=False, indent=2) + '\n')
    card['data']['extensions']['expressions'] = {m: f'expressions/{slug}/{m}.webp' for m in MOODS}
    path.write_text(json.dumps(card, ensure_ascii=False, indent=2) + '\n')
    embed(path.with_suffix('.png'), card)
    gateway = copy.deepcopy(card)
    gateway['data']['extensions']['expressions'] = {m: BASE + f'presets/{group}/expressions/{slug}/{m}.webp' for m in MOODS}
    gateway_path = ROOT / 'cards_gateway' / f'{slug}.png'
    embed(gateway_path, gateway)
    changed = copy.deepcopy(card)
    if 'expressions' in original['data']['extensions']:
        changed['data']['extensions']['expressions'] = original['data']['extensions']['expressions']
    else:
        del changed['data']['extensions']['expressions']
    assert changed == original, 'Profiltexte verändert'
    validate(group, slug)
    roadmap((group, slug))
    preview = Image.new('RGB', (1200,330), '#eeeeee')
    draw = ImageDraw.Draw(preview)
    for column, mood in enumerate(MOODS):
        with Image.open(directory / (mood + '.webp')) as image:
            preview.paste(ImageOps.fit(image, (200,300)), (200*column,30))
        draw.text((200*column+5,5), mood, fill='black')
    preview.save(f'/tmp/{slug}-expressions-preview.png')
    print(f'{card["data"]["name"]}: Paket, PNG-Payloads und Roadmap aktualisiert.')

def validate(group, slug):
    path = ROOT / 'presets' / group / f'{slug}.json'
    card = json.loads(path.read_text())
    assert complete(group, slug)
    assert read_card(path.with_suffix('.png')) == card
    gateway_path = ROOT / 'cards_gateway' / f'{slug}.png'
    gateway = read_card(gateway_path)
    expected = copy.deepcopy(card)
    expected['data']['extensions']['expressions'] = {m: BASE + f'presets/{group}/expressions/{slug}/{m}.webp' for m in MOODS}
    assert gateway == expected
    hashes = set()
    for source in card['data']['extensions']['expressions'].values():
        image_path = path.parent / source
        with Image.open(image_path) as image:
            image.load()
            assert image.size == (640,800) and image.format == 'WEBP'
        hashes.add(hashlib.sha256(image_path.read_bytes()).digest())
    assert len(hashes) == 6, 'Doppelte Emotionsbilder'
    print(f'OK: {slug}, sechs WebPs, unveränderte Profiltexte, konsistente V2-Karten und Hub-URLs.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('group', choices=CAST)
    parser.add_argument('slug')
    parser.add_argument('--manifest')
    args = parser.parse_args()
    assert args.slug in CAST[args.group]
    if args.manifest:
        package(args.group, args.slug, args.manifest)
    else:
        validate(args.group, args.slug)
