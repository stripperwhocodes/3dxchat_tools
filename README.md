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
gentext.py "some cool text" > my_world.world
```

See `gentext.py --help` for options

Simple tool to move (translate) the world along x, y, z axes. It comes handy if you
have a downloaded item to merge into your world but the distance between the
item's location and where you want it is large. You can move one world by desired
offset and then merge. Another good use is the workaround for the sea level that
keeps resetting on you. If you are tired of constantly having to set the sea level
before opening the room, just move the world by the necessary y-offset.
Use it like this:

## World mover

```
moveworld.py -x <offset> -y <offset> -z <offset> my_world.world > my_new_world.world
```

See `moveworld.py --help` for options.

## Picture to world converter

Simple tool to convert the picture to 3dxchat world. This is still work in progress
and there are not too many options for image pre-processing. There is a more complete
tool (for windows) available but when I add more options this will become an alternative.
Use it like this:

```
pic23dxchat.py my_sexy_image.png > my_sexy_image.world
```

See `pic23dxchat.py --help` for options.
