#!/usr/bin/env python
import qrcode
import qrcode.image.svg
import io

import xml.etree.ElementTree as ET

data = "https://docs.python.org/"

factory = qrcode.image.svg.SvgFragmentImage
img = qrcode.make(data, image_factory = factory)

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
        x = float(child.attrib['x'].replace('mm', ''))
        y = float(child.attrib['y'].replace('mm', ''))
        width = float(child.attrib['width'].replace('mm', ''))
        height = float(child.attrib['height'].replace('mm', ''))
        new_box = {
            "n": "Box",
            "p": [ x, y, 0.0],
            "r": [ 0.0, 0.0, 0.0],
            "s": [ width, height, 0.1 ],
            "c": [ 0.0, 0.0, 0.0],
            "m": "unlit"
        }
        world["objects"][0]["objects"].append(new_box)
print(world)
