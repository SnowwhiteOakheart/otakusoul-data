import json
import os
import base64
from PIL import Image, PngImagePlugin

DATA_DIR = "/home/deathtrap/development/otakusoul-data/presets/no-game-no-life"

for filename in os.listdir(DATA_DIR):
    if filename.endswith(".json") and not filename.startswith("persona_"):
        json_path = os.path.join(DATA_DIR, filename)
        png_path = os.path.join(DATA_DIR, filename.replace('.json', '.png'))
        if os.path.exists(png_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                card_data = json.load(f)
            im = Image.open(png_path)
            meta = PngImagePlugin.PngInfo()
            json_bytes = json.dumps(card_data, ensure_ascii=False).encode('utf-8')
            b64_str = base64.b64encode(json_bytes).decode('ascii')
            meta.add_text("chara", b64_str)
            im.save(png_path, "PNG", pnginfo=meta)
            
            # Update gateway as well
            gateway_path = os.path.join("/home/deathtrap/development/otakusoul-data/cards_gateway", filename.replace('.json', '.png').replace('chlammy_zell', 'Chlammy_Zell').replace('fiel_nirvalen', 'Fiel_Nirvalen').replace('izuna_hatsuse', 'Izuna_Hatsuse').replace('jibril', 'Jibril').replace('stephanie_dola', 'Stephanie_Dola').replace('shiro', 'Shiro').replace('sora', 'Sora'))
            if os.path.exists(gateway_path):
                im.save(gateway_path, "PNG", pnginfo=meta)
            print(f"Injected {filename}")
