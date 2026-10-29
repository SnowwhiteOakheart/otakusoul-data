"""Exports THA3 (standard_float) as one ONNX graph: image (1,4,512,512) in -1..1 with alpha,
pose (1,45) -> posed image (1,4,512,512). Same steps as FiveStepPoserComputationProtocol, without
caching and in-place writes. Usage: export_onnx.py <tha3 code dir> <out.onnx> [variant]"""
import sys
import time
from pathlib import Path

CODE, OUT = Path(sys.argv[1]), Path(sys.argv[2])
VARIANT = sys.argv[3] if len(sys.argv) > 3 else 'standard_float'
sys.path.insert(0, str(CODE))
import os
os.chdir(CODE)

import numpy as np
import torch
from torch import nn
from torch.nn.functional import interpolate
from tha3.poser.modes.load_poser import load_poser

poser = load_poser(VARIANT, torch.device('cpu'))
modules = poser.get_modules()
EYEBROW, FACE = 12, 27


class Tha3(nn.Module):
    def __init__(self):
        super().__init__()
        self.decomposer = modules['eyebrow_decomposer']
        self.combiner = modules['eyebrow_morphing_combiner']
        self.face = modules['face_morpher']
        self.rotator = modules['two_algo_face_body_rotator']
        self.editor = modules['editor']

    def forward(self, image, pose):
        eyebrow_pose = pose[:, :EYEBROW]
        face_pose = pose[:, EYEBROW:EYEBROW + FACE]
        rotation_pose = pose[:, EYEBROW + FACE:]
        # Eyebrows: the 128 px head box.
        decomposed = self.decomposer(image[:, :, 64:192, 192:320])
        combined = self.combiner(decomposed[3], decomposed[0], eyebrow_pose)  # background, eyebrow layer
        eyebrow_morphed = combined[2]  # eyebrow_morphed_image_index (standard: 2)
        # Face: the 192 px box around it, with the morphed eyebrows pasted in the middle.
        face_box = image[:, :, 32:224, 160:352]
        middle = torch.cat([face_box[:, :, 32:160, :32], eyebrow_morphed, face_box[:, :, 32:160, 160:]], dim=3)
        face_in = torch.cat([face_box[:, :, :32], middle, face_box[:, :, 160:]], dim=2)
        face_morphed = self.face(face_in, face_pose)[0]
        # Face back into the whole image.
        row = torch.cat([image[:, :, 32:224, :160], face_morphed, image[:, :, 32:224, 352:]], dim=3)
        full = torch.cat([image[:, :, :32], row, image[:, :, 224:]], dim=2)
        half = interpolate(full, size=(256, 256), mode='bilinear', align_corners=False)
        rotated = self.rotator(half, rotation_pose)
        warped = interpolate(rotated[1], size=(512, 512), mode='bilinear', align_corners=False)
        grid = interpolate(rotated[2], size=(512, 512), mode='bilinear', align_corners=False)
        return self.editor(full, warped, grid, rotation_pose)[0]


model = Tha3().eval()
image = torch.rand(1, 4, 512, 512) * 2 - 1
pose = torch.rand(1, 45) * 0.8
with torch.no_grad():
    expected = poser.pose(image, pose[0], 0).unsqueeze(0) if poser.pose(image, pose[0], 0).dim() == 3 else poser.pose(image, pose[0], 0)
    mine = model(image, pose)
print('wrapper vs poser max diff:', float((expected - mine).abs().max()))
torch.onnx.export(model, (image, pose), str(OUT), input_names=['image', 'pose'], output_names=['output'],
                  opset_version=20, dynamo=False)
print('exported', OUT, OUT.stat().st_size // 1024 // 1024, 'MB')

import onnxruntime as ort
session = ort.InferenceSession(str(OUT), providers=['CPUExecutionProvider'])
start = time.perf_counter()
result = session.run(None, {'image': image.numpy(), 'pose': pose.numpy()})[0]
print('onnx vs torch max diff:', float(np.abs(result - mine.numpy()).max()), f'CPU {time.perf_counter() - start:.2f}s first run')
start = time.perf_counter()
for _ in range(3):
    session.run(None, {'image': image.numpy(), 'pose': pose.numpy()})
print(f'CPU {(time.perf_counter() - start) / 3:.2f}s per pose')
