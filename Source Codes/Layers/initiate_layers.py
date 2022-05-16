import rhinoscriptsyntax as rs
import scriptcontext as sc
from System.Drawing import Color
import Rhino

def OLD_add_material(name, RGBAR):
    red, green, blue, transparency, reflectivity = RGBAR # trnasparency 0 = solid, 1 = see-thru
    # Create a Rhino material.
    rhino_material = Rhino.DocObjects.Material();
    rhino_material.Name = name;
    rhino_material.DiffuseColor = Color.FromArgb(red,green,blue)
    rhino_material.Transparency = transparency
    rhino_material.ToPhysicallyBased()


    # Use the Rhino material to create a Render material.
    render_material = Rhino.Render.RenderMaterial.CreateBasicMaterial(rhino_material, sc.doc)
    render_material = sc.doc.RenderMaterials.Add(render_material)

def OLD_modify_material(material_index, RGBAR):
    red, green, blue, transparency, reflectivity = RGBAR # trnasparency 0 = solid, 1 = see-thru,,,,,reflectivity 0 = matte, 255 = glossy

    rs.MaterialColor(material_index, color = Color.FromArgb(red,green,blue))
    rs.MaterialTransparency(material_index, transparency = transparency)
    rs.MaterialShine( material_index, shine = reflectivity )
    rs.MaterialReflectiveColor(material_index, color = rs.ColorHLSToRGB( (0, 255*reflectivity, 0) ))


def modify_material(material_name, RGBAR):
    material = get_material_by_name(material_name)

    print "begin changing material = {}".format(material)
    red, green, blue, transparency, reflectivity = RGBAR # trnasparency 0 = solid, 1 = see-thru,,,,,reflectivity 0 = matte, 255 = glossy
    material.DiffuseColor = Color.FromArgb(red,green,blue)
    material.Transparency = transparency
    material.TransparentColor = Color.FromArgb(red,green,blue)
    material.Reflectivity = reflectivity
    material.ReflectionGlossiness = reflectivity
    print "changing complete\n."


def get_material_by_name(name):
    all_mats = sc.doc.Materials
    for mat in all_mats:
        print "searching", name, "found", mat.Name, "and its id = ", mat.MaterialIndex
        if mat.Name == name:
            print "##get match"
            return mat

    #if not found then create one
    mat = Rhino.DocObjects.Material();
    mat.Name = name
    return mat




def get_color(tuple):
    red, green, blue = tuple
    return Color.FromArgb(red,green,blue)


def initiate_layers():
    options = ["Facade Layer Scheme", "Program Blocks Layer Scheme"]
    new_layer_scheme_options = rs.ListBox(items = options,
                                    message= "select layer scheme option from below",
                                    title = "New Layer Scheme")
    if new_layer_scheme_options == options[0]:
        parent_layer = "EA_Facade"
        scheme_layer_options = [["Glass", (162, 195, 208)],
                                ["Metal", (195, 162, 208)],
                                ["Mullion", (182 , 189, 186)],
                                ["Shadowbox", (121, 146, 167)]]
    elif new_layer_scheme_options == options[1]:
        parent_layer = "EA_Program"
        scheme_layer_options = [["Office", (156, 211, 223)],
                                ["Retail", (241, 226, 142)],
                                ["MEP", (176 , 176, 176)],
                                ["Resi", (226, 89, 49)]]

    else:
        return

    options = [[x[0], True] for x in scheme_layer_options]
    res = rs.CheckListBox(items = options, message = "select sublayers for '{}'".format(parent_layer), title = "Initiating Layer Structure")
    print res

    for option, state in res:
        if state:
            for data in scheme_layer_options:
                layer_name, color = data
                if option == layer_name:
                    full_layer_name = "{}::{}".format(parent_layer, layer_name)
                    rs.AddLayer(name = full_layer_name,
                                color = get_color(color),
                                parent = None)

                    continue





                    r,g,b = color

                    if has_any_keyword(layer_name, ["glass"]):
                        t = 0.9
                    else:
                        t = 0.0

                    if has_any_keyword(layer_name, ["glass", "metal", "water"]):
                        R = 250
                    else:
                        R = 0

                    RGBAR = (r,g,b,t,R)

                    #add_material(layer_name, RGBA)

                    # get current material index, if not having, then make new material index. This new index will be used to change name so they leave in the system
                    index = rs.LayerMaterialIndex(full_layer_name)
                    if index == -1: index = rs.AddMaterialToLayer(full_layer_name)
                    print "*******material index for layer", layer_name, " = ", index


                    # change empty new material name to match layer name
                    previous_material_name = rs.MaterialName( index, name = layer_name )
                    material_name = layer_name
                    print "--", layer_name

                    print "++", str(get_material_by_name(layer_name ))

                    #change the definition in the new material
                    modify_material( material_name, RGBAR)

                    #assign the modifed material to original layers by material index
                    rs.LayerMaterialIndex(full_layer_name, get_material_by_name(material_name).MaterialIndex)
                    continue



def has_any_keyword(input, keywords):
    for keyword in keywords:
        if keyword in input.lower():
            return True
    return False


##########################################################################

if( __name__ == "__main__" ):

  initiate_layers()
