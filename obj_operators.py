import bpy
import os


def symlink(source, link_name):
    import os
    os_symlink = getattr(os, "symlink", None)
    if callable(os_symlink):
        os_symlink(source, link_name)
    else:
        import ctypes
        csl = ctypes.windll.kernel32.CreateSymbolicLinkW
        csl.argtypes = (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32)
        csl.restype = ctypes.c_ubyte
        flags = 1 if os.path.isdir(source) else 0
        if csl(link_name, source, flags) == 0:
            raise ctypes.WinError()


def suffix_filename(path, index):
    path_stripped = path[:-5]
    return path_stripped + "link_{:03d}".format(index) + ".blend"


def create_link_file(source):
    print(source)
    for index in range(0, 99):
        target = suffix_filename(source, index)
        if not os.path.exists(target):
            symlink(source, target)
            print("Symlink created from ", source, " to ", target)
            return target
    print("Error, invalid target")


def open_link_file(source, context):
    target = create_link_file(source)
    result = bpy.ops.wm.link('INVOKE_DEFAULT', filepath=target)


class SYMLINK_OT_CreateLink(bpy.types.Operator):
    """ Creates a symlink to the requested file """
    bl_idname = "symlink.create_link"
    bl_label = "Create Symlink"
    bl_description = "Create a symlink (fake copy) of target file"
    bl_options = {'REGISTER'}

    filepath: bpy.props.StringProperty(subtype='FILE_PATH')

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        create_link_file(self.filepath)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


class SYMLINK_OT_LinkNew(bpy.types.Operator):
    """ Creates and links from the linked file """
    bl_idname = "symlink.link_import"
    bl_label = "Link Symlink"
    bl_description = "Link from a file again by creating a symlink"
    bl_options = {'REGISTER'}

    filepath: bpy.props.StringProperty(subtype='FILE_PATH')


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        open_link_file(self.filepath, context)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}