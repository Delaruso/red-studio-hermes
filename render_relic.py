
import bpy

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create Sphere
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
obj = bpy.context.active_object
bpy.ops.object.shade_smooth()

# Subdivision
subsurf = obj.modifiers.new(name='Subdiv', type='SUBSURF')
subsurf.levels = 2
subsurf.render_levels = 3

# Obsidian Material
mat_obsidian = bpy.data.materials.new(name='Obsidian')
mat_obsidian.use_nodes = True
nodes = mat_obsidian.node_tree.nodes
bsdf = nodes.get('Principled BSDF')
# Use indices to avoid version-specific key errors
bsdf.inputs[0].default_value = (0.005, 0.005, 0.005, 1) # Base Color
bsdf.inputs[2].default_value = 1.0 # Metallic
bsdf.inputs[3].default_value = 0.05 # Roughness
obj.data.materials.append(mat_obsidian)

# Red Vein Material
mat_red = bpy.data.materials.new(name='RedVein')
mat_red.use_nodes = True
nodes_red = mat_red.node_tree.nodes
for n in nodes_red:
    if n.type == 'BSDF_PRINCIPLED':
        nodes_red.remove(n)

emission = nodes_red.new(type='ShaderNodeEmission')
emission.inputs[0].default_value = (1, 0, 0, 1)
emission.inputs[1].default_value = 20.0
output = nodes_red.get('Material Output')
mat_red.node_tree.links.new(emission.outputs[0], output.inputs[0])
obj.data.materials.append(mat_red)

# Assign vein pattern
for poly in obj.data.polygons:
    if poly.index % 12 == 0:
        poly.material_index = 1

# Lighting
bpy.ops.object.light_add(type='AREA', radius=5, location=(3, -3, 4))
light = bpy.context.active_object
light.data.energy = 1000

# World
bpy.data.worlds['World'].node_tree.nodes['Background'].inputs[0].default_value = (0, 0, 0, 1)

# --- ADD CAMERA (Fixes previous error) ---
bpy.ops.object.camera_add(location=(5, -5, 3), rotation=(1.1, 0, 0.78))
bpy.context.scene.camera = bpy.context.active_object

# Render Settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 64 
bpy.context.scene.render.filepath = "/home/sky/red studio hermes/Relic_01.png"
bpy.context.scene.render.image_settings.file_format = 'PNG'

# Render
bpy.ops.render.render(write_still=True)
