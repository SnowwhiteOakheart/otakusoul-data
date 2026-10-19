#!/usr/bin/env python3
"""Ergänzt fehlende Emotionsbilder einer bestehenden Karte aus einem Generierungsmanifest.

Aufruf: python3 tools/add_expression_slots.py /tmp/<manifest>.json
Manifest: group, slug, card, gateway, reference, expressions={slot: {path, prompt}}.
Erstellt selbst keine Bilder; vorhandene Bilder, Profiltexte und PNG-Pixel bleiben erhalten.
"""
import argparse
import copy
import hashlib
import json
import shutil
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps
from package_campaign_expressions import embed, read_card

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://raw.githubusercontent.com/SnowwhiteOakheart/otakusoul-data/main/'
SLOTS = {'neutral', 'happy', 'sad', 'angry', 'surprised', 'relaxed', 'blush',
         'teasing', 'fear', 'disgust', 'crying', 'seductive', 'aroused', 'ecstasy', 'afterglow'}
SEMANTICS = {
    'seductive': 'SFW: höflich-selbstsicherer Empfang, keine sexuelle Verführung',
    'aroused': 'SFW: erhöhte Aufmerksamkeit vor einer Aufgabe, keine sexuelle Erregung',
    'ecstasy': 'SFW: überschwängliche Freude nach einem Erfolg',
    'afterglow': 'SFW: Erleichterung und Ruhe nach einer bewältigten Aufgabe',
}


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def pixels(path):
    with Image.open(path) as image:
        return image.size, image.mode, hashlib.sha256(image.tobytes()).hexdigest()


def package(manifest):
    record = json.loads(Path(manifest).read_text())
    allow_new = record.get('allow_new_series') is True
    path = ROOT / record['card']
    assert path == ROOT / 'presets' / record['group'] / (record['slug'] + '.json')
    card = json.loads(path.read_text())
    original = copy.deepcopy(card)
    expressions = card['data']['extensions'].get('expressions')
    assert expressions or allow_new, 'Neue Serien benötigen allow_new_series im Manifest'
    if not expressions:
        expressions = card['data']['extensions']['expressions'] = {}
    additions = record['expressions']
    assert set(additions) == SLOTS - set(expressions), 'Manifest muss alle fehlenden Slots enthalten'
    assert not record.get('errors'), 'Generierungsfehler zuerst beheben'
    directory = path.parent / 'expressions' / record['slug']
    targets = {m: directory / (m + '.webp') for m in additions}
    assert all(not p.exists() for p in targets.values()), 'Vorhandene Bilder niemals überschreiben'
    prompt_path = directory / 'additional_prompts.json'
    assert not prompt_path.exists(), 'Bestehenden Promptnachweis erhalten'
    png = path.with_suffix('.png')
    gateway_path = ROOT / record['gateway']
    gateway = read_card(gateway_path)
    assert gateway is not None and read_card(png) == original
    old_pixels = {p: pixels(p) for p in (png, gateway_path)}
    old_images = {relative: hashlib.sha256((path.parent / relative).read_bytes()).hexdigest()
                  for relative in expressions.values() if not relative.startswith(('https:', 'http:', 'data:'))}
    sources = []
    for mood, item in additions.items():
        with Image.open(item['path']) as image:
            image.load()
            sources.append((mood, ImageOps.fit(image.convert('RGB'), (640, 800),
                            method=Image.Resampling.LANCZOS, centering=(0.5, 0))))
    directory.mkdir(parents=True, exist_ok=True)
    supporting = record.get('supporting_reference')
    if supporting:
        reference_target = directory / 'reference_sfw.png'
        assert not reference_target.exists()
        shutil.copy2(supporting['path'], reference_target)
    for mood, image in sources:
        image.save(targets[mood], quality=92)
        expressions[mood] = f'expressions/{record["slug"]}/{mood}.webp'
        gateway['data']['extensions'].setdefault('expressions', {})[mood] = (
            BASE + f'presets/{record["group"]}/expressions/{record["slug"]}/{mood}.webp')
    assert len({hashlib.sha256(p.read_bytes()).digest() for p in targets.values()}) == len(additions)
    write_json(prompt_path, {
        'tool': 'OpenAI image_gen (eingebaut)', 'date': record.get('date', date.today().isoformat()),
        'generation_dates': {m: item.get('date', record.get('date', date.today().isoformat()))
                             for m, item in additions.items()},
        'reference': 'reference_sfw.png' if supporting else f'../../{record["slug"]}.png',
        'original_reference': f'../../{record["slug"]}.png',
        'references_by_slot': record.get('references_by_slot', {
            m: 'reference_sfw.png' if supporting else f'../../{record["slug"]}.png'
            for m in additions}),
        'reference_edit_prompt': supporting['prompt'] if supporting else None,
        'reference_note': 'Vorhandenes KI-Fanart-Porträt; Identität, Alter, Kleidung und Stil erhalten.',
        'prompts': {m: item['prompt'] for m, item in additions.items()},
        'slot_semantics': SEMANTICS,
        'postprocessing': 'Oben ausgerichteter Lanczos-Ausschnitt auf 640×800 WebP, Qualität 92. '
                          'Bestehende Porträtpixel und Emotionsbilder bleiben unverändert.',
        'provenance': 'Inoffizielle KI-generierte Fanart; vorhandene Herkunfts- und Rechtehinweise '
                      'des jeweiligen Pakets gelten weiter. Alle Varianten sind nichtsexuell und altersgerecht.',
    })
    restored = copy.deepcopy(card)
    if 'expressions' in original['data']['extensions']:
        restored['data']['extensions']['expressions'] = original['data']['extensions']['expressions']
    else:
        restored['data']['extensions'].pop('expressions', None)
    assert restored == original, 'Profiltexte oder sonstige Metadaten verändert'
    write_json(path, card)
    embed(png, card)
    embed(gateway_path, gateway)
    assert read_card(png) == card and read_card(gateway_path) == gateway
    assert all(pixels(p) == value for p, value in old_pixels.items()), 'Porträtpixel verändert'
    assert all(hashlib.sha256((path.parent / rel).read_bytes()).hexdigest() == value
               for rel, value in old_images.items()), 'Bestehende Emotion verändert'
    registry_path = ROOT / 'soul_registry.json'
    registry = json.loads(registry_path.read_text())
    entry = next(e for e in registry['characters'] if e['name'] == card['data']['name'])
    entry['revision'] += 1
    entry['updated'] = record.get('date', date.today().isoformat())
    write_json(registry_path, registry)
    roadmap_path = ROOT / 'ROADMAP.md'
    text = roadmap_path.read_text()
    marker = ('### NTE – vollständige Emotionsserien' if allow_new
              else '### Zusatzemotionen – bestehende Figuren (ohne NTE)')
    if marker not in text:
        text += '\n\n' + marker + '\n\n'
        text += ('Acht NTE-Figuren erhalten auf Auftrag vom 19.10.2026 je 15 Bilder (120 insgesamt).\n\n'
                 if allow_new else '49 bestehende Figuren erhalten je neun Zusatzbilder.\n\n')
    text += f'- [x] **{card["data"]["name"]}** ({record["group"]}): alle 15 Slots, '
    text += f'{len(additions)} neue eigenständige SFW-Bilder, Promptnachweis und PNG-/Hub-Metadaten geprüft.\n'
    roadmap_path.write_text(text)
    preview = Image.new('RGB', (750, ((len(sources) + 2) // 3) * 340), '#eeeeee')
    draw = ImageDraw.Draw(preview)
    for n, (mood, image) in enumerate(sources):
        preview.paste(image.resize((250, 313)), ((n % 3) * 250, (n // 3) * 340 + 25))
        draw.text(((n % 3) * 250 + 5, (n // 3) * 340 + 5), mood, fill='black')
    preview_path = Path('/tmp') / (record['slug'] + '-additional-preview.jpg')
    preview.save(preview_path)
    print(f'{card["data"]["name"]}: {len(additions)} Zusatzbilder; alle 15 Slots; '
          f'Profiltexte, alte Emotionen und Porträtpixel unverändert. Vorschau: {preview_path}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest')
    package(parser.parse_args().manifest)
