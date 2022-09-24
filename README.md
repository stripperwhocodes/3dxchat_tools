# Usage

All tools are meant to run from command line. You need Python. If you are on Linux or Mac,
Python should be already installed. If you are on Windows, you can either install Python
for Windows or enable WSL (Windows Subsystem for Linux).

# Available tools

## Text generator

This tool comes handy if you want to put some text into your world. Generate the text
using the tool and then merge into your world. For now only Soda font is supported.
Other fonts will be added later. Use it like this:

```
gentext.py -o my_world.world "some cool text"
```

See `gentext.py --help` for options

## World mover

Simple tool to move (translate) the world along x, y, z axes. It comes handy if you
have a downloaded item to merge into your world but the distance between the
item's location and where you want it is large. You can move one world by desired
offset and then merge. Another good use is the workaround for the sea level that
keeps resetting on you. If you are tired of constantly having to set the sea level
before opening the room, just move the world by the necessary y-offset.
Use it like this:


```
moveworld.py -o my_moved_world.world -x <offset> -y <offset> -z <offset> my_world.world
```

See `moveworld.py --help` for options.

## Color picker

This tool is useful to pick the color of an object. Open the world editor and select
the object of interest and note its approximate coordinates. Then run the tool and give
it the coordinate and the search radius. The search radius depends on the accuracy of
your coordinates. For example, if you enter only two decimal places, then your
search radius should be at least 0.01. Use it like this:

```
getcolors.py -x <x_pos> -y <y_pos> -z <z_pos> -r <radius> my_world.world
```

## Material picker

Similar too to color picker, but reports materials for all objects in the vicinity
of specified coordinates. Use it like this:

```
getmaterials.py -x <x_pos> -y <y_pos> -z <z_pos> -r <radius> my_world.world
```

## Picture to world converter

Simple tool to convert the picture to 3dxchat world. This is still work in progress
and there are not too many options for image pre-processing. There is a more complete
tool (for windows) available but when I add more options this will become an alternative.
Use it like this:

```
pic23dxchat.py -o my_world.world my_sexy_image.png
```

See `pic23dxchat.py --help` for options.
