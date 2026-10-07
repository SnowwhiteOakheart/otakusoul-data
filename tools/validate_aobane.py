"""Prüft das Aobane-Paket ohne Installation oder Netzwerkanfragen."""
import base64
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = 'https://raw.githubusercontent.com/SnowwhiteOakheart/otakusoul-data/main/'
MOODS = {'neutral', 'happy', 'relaxed', 'surprised', 'angry', 'sad'}
FIELDS = ('name', 'description', 'personality', 'scenario', 'first_mes', 'mes_example',
          'creator_notes', 'system_prompt', 'post_history_instructions', 'custom_title', 'tags')

def png_card(path):
    with Image.open(path) as image:
        image.load()
        assert image.size == (700, 937), path
        return json.loads(base64.b64decode(image.info['chara']))

def validate():
    registry = json.loads((ROOT / 'soul_registry.json').read_text())['characters']
    names = [entry['name'] for entry in registry]
    assert len(names) == len(set(names)), 'Doppelte Hub-Namen'
    for slug in ('ren_takahashi', 'aoi_mizuno'):
        path = ROOT / 'presets/aobane-highschool' / f'{slug}.json'
        card = json.loads(path.read_text())
        assert card['spec'] == 'chara_card_v2' and card['spec_version'] == '2.0'
        data = card['data']
        ext = data['extensions']
        assert ext['otakusoul_i18n']['source_language'] == 'de'
        assert set(ext['otakusoul_i18n']['translations']) == {'en', 'ru'}
        locales = {'de': {**data, 'custom_title': ext['custom_title']}, **ext['otakusoul_i18n']['translations']}
        for lang, fields in locales.items():
            for field in FIELDS:
                assert fields.get(field), (slug, lang, field)
            assert len(fields['description']) >= 1200, (slug, lang, 'Profilumfang')
            assert len(fields['alternate_greetings']) >= 2
            assert fields['mes_example'].count('<START>') >= 3
            assert '# Role & Identity' in fields['system_prompt']
            assert '{{user}}' in fields['first_mes'] and '{{char}}' in fields['system_prompt']
        assert set(ext['expressions']) == MOODS
        for mood, source in ext['expressions'].items():
            with Image.open(path.parent / source) as image:
                image.load()
                assert image.format == 'WEBP' and image.size == (640, 800), (slug, mood)
        assert png_card(path.with_suffix('.png')) == card, 'JSON/PNG unterscheiden sich'
        gateway_name = data['name'].replace(' ', '_') + '.png'
        gateway = png_card(ROOT / 'cards_gateway' / gateway_name)
        for source in gateway['data']['extensions']['expressions'].values():
            assert source.startswith(BASE_URL)
            assert (ROOT / source.removeprefix(BASE_URL)).is_file(), source
        gateway['data']['extensions']['expressions'] = ext['expressions']
        assert gateway == card
        entry = next(e for e in registry if e['name'] == data['name'])
        assert entry['download_url'] == BASE_URL + 'cards_gateway/' + gateway_name
    print('OK: zwei Profile, DE/EN/RU, zwölf Expressions, V2-Payloads und Hub-Pfade.')

if __name__ == '__main__':
    validate()
