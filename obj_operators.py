import bpy


class SYMLINK_OT_CreateLink(bpy.types.Operator):
    """ Creates a symlink to the requested file """
    bl_idname = "symlink.create_link"
    bl_label = "Create symlink to source"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        return {'FINISHED'}
