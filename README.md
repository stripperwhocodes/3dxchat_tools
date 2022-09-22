# Usage

All tools are meant to run from command line. You need Python. If you are on Linux or Mac,
Python should be already installed. If you are on Windows, you can either install Python
for Windows or enable WSL (Windows Subsystem for Linux).

# Available tools

Simple tool to convert the picture to 3dxchat world. Use it like this:

```
pic23dxchat.py my_sexy_image.png > my_sexy_image.world
```

See `pic23dxchat.py --help` for options.


Simple tool to generate a world with text in Soda font. Use it like this:

```
gentext.py "come cool text" > my_world.world
```

See `gentext.py --help` for options

Simple tool to move (translate) the world along x, y, z axes. Use it like this:

```
moveworld.py -x <offset> -y <offset> -z <offset> my_world.world > my_new_world.world
```

See `moveworld.py -- help` for option.
