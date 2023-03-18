#!/usr/bin/env python
import qrcode
import qrcode.image.svg
import io
import argparse
import json

import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description = 'generate the world file with QR code')
parser.add_argument('url', type=str, help='url to put in the QR code')
parser.add_argument('--resize', '-r', type=float, default=1.0, help='resize factor')
parser.add_argument('--output_file', '-o', type=str, default='', help='output file')
args = parser.parse_args()

factory = qrcode.image.svg.SvgFragmentImage
img = qrcode.make(args.url, image_factory = factory)

# save svg file to tmp, and load it back as svg
img.save('tmp.svg')

# svg is just xml, and we only have rectangles, so parsing is simple
tree = ET.parse('tmp.svg')
root = tree.getroot()

# create world template, with spawner only and one empty group
world = {
    "respawn":{
        "p": [0.0,1.0,-5.0],
        "r": 180.0
    },
    "ambient": [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
    "oceanlevel": 0.0,
    "weather": "Day",
    "valuetype": "float",
    "objects": [
        {
            "n": "group",
            "objects" : []
        }
    ]
}

for child in root:
    if child.tag.endswith('rect'):
        x = float(child.attrib['x'].replace('mm', '')) * args.resize
        y = float(child.attrib['y'].replace('mm', '')) * args.resize
        width = float(child.attrib['width'].replace('mm', '')) * args.resize
        height = float(child.attrib['height'].replace('mm', '')) * args.resize
        new_box = {
            "n": "Box",
            "p": [ x, y, 0.0],
            "r": [ 0.0, 0.0, 0.0],
            "s": [ width, height, 0.1 ],
            "c": [ 0.0, 0.0, 0.0],
            "m": "unlit"
        }
        world["objects"][0]["objects"].append(new_box)

if not args.output_file:
    print(world)
else:
    with open(args.output_file, 'w') as f:
        f.write(json.dumps(world, indent=None))
