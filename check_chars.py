import json
import glob
import sys
import os

def check_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        cdata = data.get('data', data) # handle if it is wrapped in 'data'
        
        name = cdata.get('name', 'Unknown')
        desc_len = len(cdata.get('description', ''))
        alt_greetings = len(cdata.get('alternate_greetings', []))
        mes_example = len(cdata.get('mes_example', ''))
        
        ext = cdata.get('extensions', {})
        i18n = ext.get('otakusoul_i18n', {})
        en = i18n.get('translations', {}).get('en', {})
        
        en_desc_len = len(en.get('description', ''))
        en_alt_len = len(en.get('alternate_greetings', []))
        en_mes = len(en.get('mes_example', ''))
        
        if en_desc_len < 1200 or en_alt_len < 2 or en_mes < 200 or alt_greetings < 2 or desc_len < 1200:
            print(f"Needs Upgrade: {filepath} ({name}) - DE Desc: {desc_len}, EN Desc: {en_desc_len}, DE Alt: {alt_greetings}, EN Alt: {en_alt_len}, DE Mes: {mes_example}, EN Mes: {en_mes}")
    except Exception as e:
        print(f"Error checking {filepath}: {e}")

for root, _, files in os.walk('/home/deathtrap/development/otakusoul-data/presets'):
    for file in files:
        if file.endswith('.json') and not file.startswith('persona_'):
            check_file(os.path.join(root, file))
