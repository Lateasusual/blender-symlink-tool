from .obj_operators import *
from .obj_panels import *

bl_info = {
    "name": "blender-symlink-tool",
    "description": "Link an item uniquely multiple times from the same source file",
    "author": "Lateasusual",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "3D View -> Sidebar -> Misc Tab",
    "category": "Import-Export"
}

classes = {
    VIEW3D_PT_SymlinkPanel,
    SYMLINK_OT_CreateLink,
    SYMLINK_OT_LinkNew
}


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
