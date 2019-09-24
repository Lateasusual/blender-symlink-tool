import bpy


class VIEW3D_PT_SymlinkPanel(bpy.types.Panel):
    """ Symlink tool panel """
    bl_label = "Symlink tool"
    bl_idname = "VIEW3D_PT_SymlinkPanel"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Misc"

    def __init__(self):
        pass

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Create a link")
        row = layout.row()
        row.operator('symlink.create_link')
        row = layout.row()
        row.label(text="Create a link and link from it")
        row = layout.row()
        row.operator('symlink.link_import')
