import bpy
import math

def clean_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    bpy.ops.outliner.orphans_purge()

def create_gold_material():
    mat = bpy.data.materials.new(name='Sovereign_Gold')
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    out = nodes.new('ShaderNodeOutputMaterial')
    principled = nodes.new('ShaderNodeBsdfPrincipled')
    principled.inputs['Metallic'].default_value = 1.0
    principled.inputs['Roughness'].default_value = 0.2
    principled.inputs['Base Color'].default_value = (0.78, 0.66, 0.33, 1.0)
    mat.node_tree.links.new(principled.outputs['BSDF'], out.inputs['Surface'])
    return mat

def create_red_emission_material():
    mat = bpy.data.materials.new(name='Signal_Red')
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    out = nodes.new('ShaderNodeOutputMaterial')
    emission = nodes.new('ShaderNodeEmission')
    emission.inputs['Color'].default_value = (1.0, 0.0, 0.004, 1.0)
    emission.inputs['Strength'].default_value = 3.0
    mat.node_tree.links.new(emission.outputs['Emission'], out.inputs['Surface'])
    return mat

def add_material(obj, mat):
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)

def icosahedron_relic(name, size=1.0, gold=True):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1, radius=size)
    obj = bpy.context.active_object
    obj.name = name
    obj.data.name = name + '_mesh'
    if gold:
        add_material(obj, create_gold_material())
    return obj

def octahedron_relic(name, size=1.0, gold=True):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=0, radius=size)
    obj = bpy.context.active_object
    obj.name = name
    obj.data.name = name + '_mesh'
    if gold:
        add_material(obj, create_gold_material())
    return obj

def torus_relic(name, radius=1.5, tube=0.05, gold=True):
    bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), major_radius=radius, minor_radius=tube)
    obj = bpy.context.active_object
    obj.name = name
    if gold:
        add_material(obj, create_gold_material())
    return obj

def diamond_relic(name, size=1.0, red=True):
    verts = [
        (0, 0, size),
        (size*0.7, 0, 0),
        (-size*0.7, 0, 0),
        (0, size*0.7, 0),
        (0, -size*0.7, 0),
        (0, 0, -size),
    ]
    edges = [(0,1),(0,2),(0,3),(0,4),(0,5),(1,3),(3,2),(2,4),(4,1),(1,5),(2,5),(3,5),(4,5)]
    mesh = bpy.data.meshes.new(name + '_mesh')
    mesh.from_pydata(verts, edges, [])
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    if red:
        add_material(obj, create_red_emission_material())
    return obj

def save_blend(filepath):
    bpy.ops.wm.save_as_mainfile(filepath=filepath)

clean_scene()
icosahedron_relic('Relic_The_Signal', size=1.2)
octahedron_relic('Relic_The_Remembrance', size=1.1)
torus_relic('Relic_The_Origin', radius=1.3, tube=0.04)
diamond_relic('Relic_The_Union', size=1.2, red=False)
torus_relic('Relic_The_Invitation', radius=1.4, tube=0.03)
save_blend('/home/sky/red studio hermes/artifacts/3d_models/sovereign_relics.blend')
