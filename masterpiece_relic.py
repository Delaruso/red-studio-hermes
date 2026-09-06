
import bpy
import random

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 1. The Monolith (Complex Geometry)
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
obj = bpy.context.active_object
obj.scale = (0.5, 0.5, 2)
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.subdivide(number_cuts=10)
# Randomly move vertices to create 'Fractured' look
import bmesh
bm = bmesh.from_edit_mesh(obj.data)
for v in bm.verts:
    if random.random() > 0.8:
        v.co.x += random.uniform(-0.2, 0.2)
        v.co.y += random.uniform(-0.2, 0.2)
bmesh.update_edit_mesh(obj.data)
bpy.ops.object.mode_set(mode='OBJECT')

# 2. The "Divine Obsidian" Material (Procedural)
mat_obsidian = bpy.data.materials.new(name='DivineObsidian')
mat_obsidian.use_nodes = True
nodes = mat_obsidian.node_tree.nodes
links = mat_obsidian.node_tree.links
# Remove default
nodes.remove(nodes.get('Principled BSDF'))

# Noise Texture for organic surface
noise = nodes.new(type='ShaderNodeTexNoise')
noise.inputs['Scale'].default_value = 10.0
noise.inputs['Detail'].default_value = 15.0

# Bump node for surface detail
bump = nodes.new(type='ShaderNodeBump')
bump.inputs['Strength'].default_value = 0.1

# Principled BSDF
bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
bsdf.inputs['Base Color'].default_value = (0.002, 0.002, 0.005, 1)
bsdf.inputs['Metallic'].default_value = 1.0
bsdf.inputs['Roughness'].default_value = 0.1

links.new(noise.outputs[0], bump.inputs[0])
links.new(bump.outputs[0], bsdf.inputs['Normal'])
links.new(bsdf.outputs[0], nodes.get('Material Output').inputs[0])
obj.data.materials.append(mat_obsidian)

# 3. The "Liquid Light" Veins
mat_liquid = bpy.data.materials.new(name='LiquidLight')
mat_liquid.use_nodes = True
nodes_liq = mat_liquid.node_tree.nodes
nodes_liq.remove(nodes_liq.get('Principled BSDF'))
emission = nodes_liq.new(type='ShaderNodeEmission')
emission.inputs['Color'].default_value = (1, 0, 0, 1)
emission.inputs['Strength'].default_value = 50.0 # Extreme glow
links_liq = mat_liquid.node_tree.links
links_liq.new(emission.outputs[0], nodes_liq.get('Material Output').inputs[0])
obj.data.materials.append(mat_liquid)

# Assign Liquid to the 'broken' parts
for poly in obj.data.polygons:
    if poly.area < 0.1 or random.random() > 0.95:
        poly.material_index = 1

# 4. Atmosphere (Volumetric Fog)
world = bpy.data.worlds['World']
world.use_nodes = True
w_nodes = world.node_tree.nodes
w_nodes.remove(w_nodes.get('Background'))
vol_cube = w_nodes.new(type='ShaderNodeVolumeDiffuse')
vol_cube.inputs['Color'].default_value = (0.01, 0, 0, 1)
vol_output = w_nodes.get('World Output')
world.node_tree.links.new(vol_cube.outputs[0], vol_output.inputs[0])

# 5. Cinematic Lighting
bpy.ops.object.light_add(type='AREA', location=(5, -5, 5))
light = bpy.context.active_object
light.data.energy = 2000
light.data.color = (1, 0.8, 0.8)

# 6. Camera & Render
bpy.ops.object.camera_add(location=(8, -8, 4), rotation=(1.1, 0, 0.78))
bpy.context.scene.camera = bpy.context.active_object

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 128
bpy.context.scene.render.filepath = "/home/sky/red studio hermes/Masterpiece_01.png"
bpy.ops.render.render(write_still=True)
