bl_info = {
    "name": "autoRender-save",
    "author": "sqien",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Properties > Scene > autoRender-save > Render&Save",
    "description": "Python script to automatically render and save an image",
    "warning": "",
    "doc_url": "https://github.com/sqien/blender-autoRender-save",
    "category": "Render",
}

import bpy
import random

def main(context):

    #resolution settings

    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080


    FILE_NAME = 'render.png'

    x = list(range(1, 1001))
    y = random.randrange(len(x))

    FILE_NAME = f'render{x[y]}.png'
    print(FILE_NAME)

    FILE_PATH = '//{}'.format(FILE_NAME)

    def render_project():
        previous_path = bpy.context.scene.render.filepath
        bpy.context.scene.render.filepath = FILE_PATH
        
        bpy.ops.render.render(write_still=True)
        bpy.context.scene.render.filepath = previous_path
        
    render_project()


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Render&Save"

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)

    #bpy.ops.object.simple_operator()


class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "autoRender-save"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Big render button
        #layout.label(text="render:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.simple_operator")



def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()
