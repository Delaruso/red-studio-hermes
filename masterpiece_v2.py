
import bpy
import random

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 1. The Monolith - Complex Jagged Pillar
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
obj = bpy.context.active_object
obj.scale = (0.6, 0.6, 2.5)
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.subdivide(number_cuts=8)

import bmesh
bm = bmesh.from_edit_mesh(obj.data)
for v in bm.verts:
    if random.random() > 0.7:
        v.co.x += random.uniform(-0.3, 0.3)
        v.co.y += random.uniform(-0.3, 0.3)
        v.co.z += random.uniform(-0.1, 0.1)
bmesh.update_edit_mesh(obj.data)
bpy.ops.object.mode_set(mode='OBJECT')

# 2. Divine Obsidian Material (Procedural High-Detail)
mat_obsidian = bpy.data.materials.new(name='DivineObsidian')
mat_obsidian.use_nodes = True
nodes = mat_obsidian.node_tree.nodes
links = mat_obsidian.node_tree.links
nodes.remove(nodes.get('Principled BSDF'))

# Noise Texture for organic surface
noise = nodes.new(type='ShaderNodeTexNoise')
noise.inputs['Scale'].default_value = 15.0
noise.inputs['Detail'].default_value = 15.0

# Bump node for surface detail
bump = nodes.new(type='ShaderNodeBump')
bump.inputs['Strength'].default_value = 0.2

# Principled BSDF
bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
bsdf.inputs[0].default_value = (0.002, 0.002, 0.005, 1) # Base Color
bsdf.inputs[2].default_value = 1.0 # Metallic
bsdf.inputs[3].default_value = 0.1 # Roughness

links.new(noise.outputs[0], bump.inputs[0])
links.new(bump.outputs[0], bsdf.inputs['Normal'])
links.new(bsdf.outputs[0], nodes.get('Material Output').inputs[0])
obj.data.materials.append(mat_obsidian)

# 3. The "Liquid Light" Veins (Extreme Emission)
mat_liquid = bpy.data.materials.new(name='LiquidLight')
mat_liquid.use_nodes = True
nodes_liq = mat_liquid.node_tree.nodes
for n in nodes_liq:
    if n.type == 'BSDF_PRINCIPLED':
        nodes_liq.remove(n)
emission = nodes_liq.new(type='ShaderNodeEmission')
emission.inputs[0].default_value = (1, 0, 0, 1)
emission.inputs[1].default_value = 100.0 
links_liq = mat_liquid.node_tree.links
links_liq.new(emission.outputs[0], nodes_liq.get('Material Output').inputs[0])
obj.data.materials.append(mat_liquid)

# Assign liquid to fragmented faces
for poly in obj.data.polygons:
    if poly.area < 0.2 or random.random() > 0.9:
        poly.material_index = 1

# 4. Cinematic Lighting & World
world = bpy.data.worlds['World']
world.use_nodes = True
world.node_tree.nodes['Background'].inputs[0].default_value = (0, 0, 0, 1)

bpy.ops.object.light_add(type='AREA', location=(5, -5, 5))
light = bpy.context.active_object
light.data.energy = 5000
light.data.color = (1, 0.9, 0.9)

# 5. High-End Camera setup
bpy.ops.object.camera_add(location=(10, -10, 5), rotation=(1.1, 0, 0.78))
bpy.context.scene.camera = bpy.context.active_object

# 6. Cycles Ultra-Quality Render
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 256 
bpy.context.scene.render.filepath = "/home/sky/red studio hermes/Masterpiece_Relic_01.png"
bpy.context.scene.render.image_settings.file_format = 'PNG'

bpy.ops.render.render(write_still=True)
