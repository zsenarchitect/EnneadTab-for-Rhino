import scriptcontext as sc
import rhinoscriptsyntax as rs
import Rhino
import sys
sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib')
import EA_UTILITY as EA


def import_selected_material():
    filename = rs.OpenFileName(title = "pick a Rhino file to import view from",
                                filter = "Rhino 3D Models (*.3dm)|*.3dm||")
    if not filename:
        return

    f = Rhino.FileIO.File3dm.Read(filename)
    if (f.AllMaterials.Count == 0):
        print "no material in this file"
        return

    print f.AllMaterials
    availible_material = [[x.Name, False] for x in f.AllMaterials]
    print availible_material
    
    try:
        availible_material.sort(key = lambda x: x[0].lower())
    except:
        pass
    print availible_material
    res = rs.CheckListBox(items = availible_material,
                        message = "select materials to import from [{}]".format(filename),
                        title = "material importer")
    """
    res = EA.select_from_list(availible_material,
                            title = "EnneadTab material importer",
                            message = "select materials to import from [{}]".format(filename),
                            muti_select = True,
                            button_names = ["Select Multiple Materials"],
                            width = 500,
                            height = 500)
    """

    picked_material_name = []
    for name, status in res:
        if status:
            picked_material_name.append(name)



    for source_material in f.AllMaterials:

        if material.Name in picked_material_name:
            """
            sphere = Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 500)
            id = sc.doc.Objects.AddSphere(sphere)
            obj = sc.doc.Objects.FindId(id)
            obj.RenderMaterial = material
            """
            
            #rs.MatchMaterial(source_material.Id
            #source_material.Name = "temp_" + source_material.Name
            material = Rhino.Render.RenderMaterial.CreateBasicMaterial(source_material, sc.doc)
            sc.doc.RenderMaterials.Add(material)
            return


if __name__ == "__main__":
    import_selected_material()
