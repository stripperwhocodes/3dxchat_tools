#!/usr/bin/env python3

import argparse
import json
import string
from copy import deepcopy

def leftmost_x(group):
    return min(o["p"][0] for o in group)

def place_group(x, y, z, group, y_anchor, z_anchor):
    placed_group = deepcopy(group)
    x_anchor = leftmost_x(group)
    for o in placed_group:
        o["p"][0] += x - x_anchor
        o["p"][1] += y - y_anchor
        o["p"][2] += z - z_anchor
    return {"n": "group", "objects": placed_group}

parser = argparse.ArgumentParser(description = "generate world file with specified text")
parser.add_argument("text", type=str, help="text to generate")
args = parser.parse_args()
font_filename = "soda_font_curated.world"
font_y_anchor = 25.3633
font_z_anchor = 26.8788
font_letter_width = 0.5
font_index = list(string.ascii_uppercase) + \
    [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0" ] + \
    list(string.ascii_lowercase) + \
    [ ".", ",", "'", '"', "`", "!", "?", ":", ";", "/", "-", "[", "]" ]
with open(font_filename) as f:
    font_data = json.load(f)
# extract only letter shapes
font_data = [ g["objects"] for g in font_data["objects"] if g["n"] == "group" ]
font_data = sorted(font_data, key=lambda letter : leftmost_x(letter))
assert len(font_index)==len(font_data), f"{len(font_index)}!={len(font_data)}"

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
    ]
}

x_pos = 0
for l in args.text:
    if l == ' ':
        x_pos+=2*font_letter_width
        continue
    try:
        index = font_index.index(l)
    except:
        index = None
    if index is not None:
        letter = place_group(x_pos, 2, 0, font_data[index], font_y_anchor, font_z_anchor)
        world["objects"].append(letter)
    x_pos+=font_letter_width
print(world)
