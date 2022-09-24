#!/usr/bin/env python3

import json
import argparse
import math

parser = argparse.ArgumentParser(description = 'get colors of objects in the vicinity of a point')
parser.add_argument('filename', type=str, help='world file name')
parser.add_argument('-x', type=float, default=0.0, help='x coordinate of the target point')
parser.add_argument('-y', type=float, default=0.0, help='y coordinate of the target point')
parser.add_argument('-z', type=float, default=0.0, help='z coordinate of the target point')
parser.add_argument('-r', type=float, default=0.0, help='search radius')

args = parser.parse_args()

with open(args.filename) as f:
    world = json.load(f)

def hexcolor(color):
    return '#' + ''.join([ '%02x'%c for c in [ int(c * 255) for c in color ]])

def distance(v1, v2):
    return math.sqrt(sum([(a - b)**2 for a, b in zip(v1, v2) ]))

def show_object_colors(objects):
    for o in objects:
        if o['n'] != 'group':
            if distance(o['p'], [args.x, args.y, args.z]) < args.r:
                color = o.get('c')
                if color is not None:
                    print(str(o['n'] + ': ' + hexcolor(color)))
        else:
            show_object_colors(o['objects'])

show_object_colors(world['objects'])
