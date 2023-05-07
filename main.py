import bpy
import random

#render = bpy.context.scene.render

bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1080


FILE_NAME = 'render.png'

x = list(range(1, 1001))
y = random.randrange(len(x))

FILE_NAME = f'render{x[y]}.png'
print(FILE_NAME)

FILE_PATH = '//{}'.format(FILE_NAME)

def render_project():
    #render()
    #print("rendering")
    
    previous_path = bpy.context.scene.render.filepath
    bpy.context.scene.render.filepath = FILE_PATH
    
    bpy.ops.render.render(write_still=True)
    bpy.context.scene.render.filepath = previous_path
    
    #print("complete")

render_project()
