import sys
import json
import base64

def extract(png_path):
    with open(png_path, "rb") as f:
        data = f.read()
    
    # PNG signature
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        print("Not a PNG")
        return
        
    idx = 8
    while idx < len(data):
        length = int.from_bytes(data[idx:idx+4], "big")
        chunk_type = data[idx+4:idx+8].decode("ascii", errors="ignore")
        chunk_data = data[idx+8:idx+8+length]
        
        if chunk_type == "tEXt":
            parts = chunk_data.split(b'\x00', 1)
            if len(parts) == 2 and parts[0] == b'chara':
                try:
                    payload = base64.b64decode(parts[1]).decode("utf-8")
                    print(json.dumps(json.loads(payload), indent=2))
                    return
                except Exception as e:
                    print("Error decoding payload:", e)
        
        idx += 12 + length

if __name__ == "__main__":
    extract(sys.argv[1])
