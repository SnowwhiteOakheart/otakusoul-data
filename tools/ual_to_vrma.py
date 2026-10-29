"""Turns clips of Quaternius' Universal Animation Library (CC0, UE mannequin rig) into VRMA files.

Each output holds the skeleton (no mesh), one animation and the VRMC_vrm_animation humanoid
map. The rest pose is set to the first frame of the library's own `A_TPose` clip, because VRMA
expects a T-pose at rest. Usage: python -I ual_to_vrma.py <UAL1_Standard.glb> <out dir>
"""
import json
import struct
import sys
from pathlib import Path

BONES = {
    'pelvis': 'hips', 'spine_01': 'spine', 'spine_02': 'chest', 'spine_03': 'upperChest',
    'neck_01': 'neck', 'Head': 'head',
}
for side, s in (('l', 'left'), ('r', 'right')):
    BONES.update({
        f'clavicle_{side}': f'{s}Shoulder', f'upperarm_{side}': f'{s}UpperArm',
        f'lowerarm_{side}': f'{s}LowerArm', f'hand_{side}': f'{s}Hand',
        f'thigh_{side}': f'{s}UpperLeg', f'calf_{side}': f'{s}LowerLeg',
        f'foot_{side}': f'{s}Foot', f'ball_{side}': f'{s}Toes',
        f'thumb_01_{side}': f'{s}ThumbMetacarpal', f'thumb_02_{side}': f'{s}ThumbProximal',
        f'thumb_03_{side}': f'{s}ThumbDistal',
    })
    for ue, vrm in (('index', 'Index'), ('middle', 'Middle'), ('ring', 'Ring'), ('pinky', 'Little')):
        for i, seg in enumerate(('Proximal', 'Intermediate', 'Distal'), 1):
            BONES[f'{ue}_0{i}_{side}'] = f'{s}{vrm}{seg}'

# Clip in the library -> file name in the pack.
CLIPS = {
    'Idle_Loop': 'idle',
    'Idle_Talking_Loop': 'talk',
    'Walk_Loop': 'walk',
    'Sitting_Idle_Loop': 'sit',
    'Jump_Start': 'jump',
    'Jump_Loop': 'fall',
    'Jump_Land': 'land',
    'Dance_Loop': 'dance',
}

COMPONENTS = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4}


def read_glb(path):
    data = Path(path).read_bytes()
    json_len = struct.unpack('<I', data[12:16])[0]
    doc = json.loads(data[20:20 + json_len])
    off = 20 + json_len
    bin_len = struct.unpack('<I', data[off:off + 4])[0]
    return doc, data[off + 8:off + 8 + bin_len]


def accessor_bytes(doc, binary, index):
    acc = doc['accessors'][index]
    view = doc['bufferViews'][acc['bufferView']]
    assert acc['componentType'] == 5126 and 'byteStride' not in view, 'only tight float accessors'
    start = view.get('byteOffset', 0) + acc.get('byteOffset', 0)
    return binary[start:start + acc['count'] * COMPONENTS[acc['type']] * 4]


def first_values(doc, binary, index):
    acc = doc['accessors'][index]
    n = COMPONENTS[acc['type']]
    return list(struct.unpack(f'<{n}f', accessor_bytes(doc, binary, index)[:n * 4]))


def convert(doc, binary, clip_name):
    anims = {a['name']: a for a in doc['animations']}
    tpose, clip = anims['A_TPose'], anims[clip_name]
    nodes = [dict(n) for n in doc['nodes']]
    for node in nodes:
        node.pop('mesh', None)
        node.pop('skin', None)
    # T-pose at rest: the first frame of A_TPose for every bone it keys.
    for ch in tpose['channels']:
        path = ch['target']['path']
        if path in ('rotation', 'translation'):
            nodes[ch['target']['node']][path] = first_values(doc, binary, tpose['samplers'][ch['sampler']]['output'])

    out_bin = bytearray()
    views, accessors = [], []

    def add(index):
        raw = accessor_bytes(doc, binary, index)
        while len(out_bin) % 4:
            out_bin.append(0)
        views.append({'buffer': 0, 'byteOffset': len(out_bin), 'byteLength': len(raw)})
        out_bin.extend(raw)
        acc = {k: v for k, v in doc['accessors'][index].items() if k not in ('bufferView', 'byteOffset')}
        acc['bufferView'] = len(views) - 1
        accessors.append(acc)
        return len(accessors) - 1

    samplers, channels, cache = [], [], {}
    for ch in clip['channels']:
        node = doc['nodes'][ch['target']['node']]
        if node.get('name') not in BONES or ch['target']['path'] == 'scale':
            continue
        # Only the hips may move; all other bones only turn.
        if ch['target']['path'] == 'translation' and node.get('name') != 'pelvis':
            continue
        src = clip['samplers'][ch['sampler']]
        for key in ('input', 'output'):
            if src[key] not in cache:
                cache[src[key]] = add(src[key])
        samplers.append({'input': cache[src['input']], 'output': cache[src['output']],
                         'interpolation': src.get('interpolation', 'LINEAR')})
        channels.append({'sampler': len(samplers) - 1, 'target': dict(ch['target'])})

    names = {n.get('name'): i for i, n in enumerate(nodes)}
    out = {
        'asset': {'version': '2.0', 'generator': 'OtakuSoul ual_to_vrma (Quaternius UAL, CC0)'},
        'scene': 0,
        'scenes': [{'nodes': [i for i, n in enumerate(doc['nodes']) if not any(i in (m.get('children') or []) for m in doc['nodes'])]}],
        'nodes': nodes,
        'animations': [{'name': clip_name, 'samplers': samplers, 'channels': channels}],
        'accessors': accessors,
        'bufferViews': views,
        'buffers': [{'byteLength': len(out_bin)}],
        'extensionsUsed': ['VRMC_vrm_animation'],
        'extensions': {'VRMC_vrm_animation': {
            'specVersion': '1.0',
            'humanoid': {'humanBones': {vrm: {'node': names[ue]} for ue, vrm in BONES.items() if ue in names}},
        }},
    }
    return out, bytes(out_bin)


def write_glb(path, doc, binary):
    js = json.dumps(doc, separators=(',', ':')).encode()
    js += b' ' * ((4 - len(js) % 4) % 4)
    binary += b'\0' * ((4 - len(binary) % 4) % 4)
    total = 12 + 8 + len(js) + 8 + len(binary)
    with open(path, 'wb') as f:
        f.write(struct.pack('<4sII', b'glTF', 2, total))
        f.write(struct.pack('<I4s', len(js), b'JSON') + js)
        f.write(struct.pack('<I4s', len(binary), b'BIN\0') + binary)


if __name__ == '__main__':
    doc, binary = read_glb(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    for clip, name in CLIPS.items():
        vrma, data = convert(doc, binary, clip)
        target = out_dir / f'ual_{name}.vrma'
        write_glb(target, vrma, data)
        print(target.name, target.stat().st_size, len(vrma['animations'][0]['channels']), 'channels')
