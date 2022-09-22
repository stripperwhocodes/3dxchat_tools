#!/usr/bin/env python3

import PIL.Image as I
import argparse
import json

parser = argparse.ArgumentParser(description = 'convert image to 3dxchat world')
parser.add_argument('filename', type=str, help='picture file name')
parser.add_argument('--resize', '-r', type=float, default=1.0, help='resize factor')
parser.add_argument('--element_size', '-e', type=float, default=0.02, help='3dx pixel-element size')
parser.add_argument('--output_file', '-o', type=str, default='', help='output file')
args = parser.parse_args()

image = I.open(args.filename)
image_rgb = image.convert('RGB')
width = int(image_rgb.width / args.resize)
height = int(image_rgb.height / args.resize)
resized_rgb_image=image.resize((width, height), I.ANTIALIAS)

# create world template, with spawner only and one empty group
world = {
    "respawn":{
        "p": [0.0,0.0,-5.0],
        "r": 0.0
    },
    "ambient": [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
    "oceanlevel": 0.0,
    "weather": "Night",
    "valuetype": "float",
    "objects": [
        {
            "n": "group",
            "objects" : []
        }
    ]
}

x = 0.0
for ix in range(width):
    y = 1.0 + height * args.element_size
    for iy in range(height):
        pixel = resized_rgb_image.getpixel((ix, iy))
        new_box = {
            "n": "Box",
            "p": [ x, y, 0.0],
            "r": [0.0, 0.0, 0.0],
            "s": [ args.element_size, args.element_size, 0.1 ],
            "c": [p/255.0 for p in pixel[0:3]],
            "m": "unlit"
        }
        world["objects"][0]["objects"].append(new_box)
        y -= args.element_size
    x += args.element_size

if not args.output_file:
    print(world)
else:
    with open(args.output_file, 'w') as f:
        f.write(json.dumps(world, indent=None))
