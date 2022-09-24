#!/usr/bin/env python3

import json
import argparse

parser = argparse.ArgumentParser(description = 'move the world by a specified offset')
parser.add_argument('filename', type=str, help='world file name')
parser.add_argument('-x', type=float, default=0.0, help='x offset')
parser.add_argument('-y', type=float, default=0.0, help='y offset')
parser.add_argument('-z', type=float, default=0.0, help='z offset')
parser.add_argument('-o', type=str, default='', help='output file')
args = parser.parse_args()

with open(args.filename) as f:
    world = json.load(f)

def move_objects(objects):
    for o in objects:
        if o['n'] != 'group':
            o['p'][0] += args.x
            o['p'][1] += args.y
            o['p'][2] += args.z
        else:
            move_objects(o['objects'])

world['respawn']['p'][0] += args.x
world['respawn']['p'][1] += args.y
world['respawn']['p'][2] += args.z
move_objects(world['objects'])

if not args.o:
    print(world)
else:
    with open(args.o, 'w') as f:
        f.write(json.dumps(world, indent=None))
