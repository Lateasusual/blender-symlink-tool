# blender-symlink-tool
A small addon to allow linking from the same source file multiple times using symbolic links

Tested on Linux and Windows.

Usage:
In the Misc tab of the 3D Viewport menu, Create Link just creates a symlinked file from the target, Link symlink creates a new link and opens the "Link library" dialogue for convenience.

**Windows requires blender to be run as Administrator to allow symlink creation**
This is because windows does not have an implementation for `os.symlink()` in python, so i had to use the Win32 API to do it: `symlink() in obj_operators.py`
