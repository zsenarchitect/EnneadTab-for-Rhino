import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

import sys
sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib')
import EA_UTILITY as EA



def map_material():
    options = ["N3", "N5", "N6", "Plot Connection"]
    res = EA.select_from_list(options,
                            title = "EnneadTab",
                            message = "Use which OST mapping?",
                            muti_select = False,
                            button_names = ["Run"])[0]

    file_path = r"I:\2135\0_BIM\10_BIM Management\10_BIM Resources\ost material mapping\ost material mapping_2135_BiliBili SH HQ_{}.txt".format(res)
    #print file_path
    datas = EA.read_txt_as_list(file_path)
    #sample_balls = []
    for data in datas:
        layer_name, revit_material_name, rhino_material_name = data.split("-->")
        #print "################"
        #print layer_name
        #print rhino_material_name

        if "glass" in rhino_material_name.lower():
            r, g, b, t, R = 137, 190, 220, 1, 255
        else:
            r, g, b, t, R = 200, 200, 200, 0, 0
        RGBAR = (r,g,b,t,R)
        existing_material = EA.get_material_by_name(rhino_material_name)
        if existing_material is not None:
            mat_index = existing_material.MaterialIndex
            sample_ball = None
        else:
            mat_index, sample_ball = EA.create_material(rhino_material_name, RGBAR, return_index = True)
        #print "*******"
        #print "new material created"
        for layer in get_OST_layers(layer_name):
            #print layer
            rs.LayerMaterialIndex(layer, mat_index)
        if sample_ball is not None:
            rs.DeleteObject(sample_ball)


        #sample_balls.append(sample_ball)


    rs.Command("_Purge _Pause _Materials=_Yes _BlockDefinitions=_No _AnnotationStyles=_No _Groups=_No _HatchPatterns=_No _Layers=_No _Linetypes=_No _Textures=_No Environments=_No _Bitmaps=_No _Enter")

def import_legend_material():
    return
    legend_file = r"C:\Users\szhang\Desktop\test Rhino material legend.3dm"

def get_OST_layers(OST):

    OST = OST.replace(".", "_")
    all_layer_names = rs.LayerNames()
    OUT = []
    for layer in all_layer_names:
        if "::" in layer:
            layer = layer.split("::")[-1]
        if OST in layer:
            OUT.append(layer)
    #print "&&&&&&"
    #print OUT
    return OUT
######################  main code below   #########
if __name__ == "__main__":
    rs.EnableRedraw(False)
    import_legend_material()
    map_material()


"""
##The Search Paths options manage locations to search for bitmaps that used for render texture and bump maps.
rs.AddSearchPath(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib\EA_UTILITY.py')


rs.FindFile(filename)
Searches for a file using Rhino's search path. Rhino will look for a
    file in the following locations:
      1. The current document's folder.
      2. Folder's specified in Options dialog, File tab.
      3. Rhino's System folders
path = rs.FindFile("Rhino.exe")
print path


res = rs.StringBox(message = "type in text", default_value = "default", title = "EnneadTab")
print res

res = rs.RealBox(message="get a number", default_number = None, title = "EnneadTab", minimum = None, maximum = None)
print res

res = rs.GetString(message = "type in text or click options", strings = ["opt_1", "opt_2", "opt_3"])
print res

res = rs.EditBox(message = "type in text", default_string = "default string", title = "EnneadTab")
print res


rs.TextOut(message = "text to display\nLine 1\nLine 2", title = "EnneadTab")


rs.MessageBox(message = "text to display", buttons= 4 | 48, title = "EnneadTab")

layer = rs.GetLayer(title = "Select Layer", layer = None, show_new_button = True, show_set_current = True)


res = rs.ListBox(items = ["opt_1", "opt_2", "opt_3"], message =  "select one from below", title = "list box", default = None)
print res

res = rs.PopupMenu(items = ["opt_1", "opt_2", "opt_3", "opt_4"], modes = [0, 1, 2, 3])
print res


res = rs.MultiListBox(items = ["opt_1", "opt_2", "opt_3"], message = "select many from below", title = "mutil list box", defaults = None)
print res

res = rs.CheckListBox(items = [["opt_1", True], ["opt_2", False], ["opt_3", True]], message = "select options from below", title = "checklist box")
print res



res = rs.ComboListBox(items = ["opt_1", "opt_2", "opt_3"], message = "select options from below", title = "combo list box")
print res
for option, state in res:
    pass

res = rs.PropertyListBox(items = ["opt_1", "opt_2", "opt_3"], values = [1, 2, 3], message = "modify property", title = "propety list box")
print res









rhino read excel, and write
http://developer.rhino3d.com/guides/rhinoscript/reading-excel-files/


print sc.doc ---> <Rhino.RhinoDoc object at 0x0000000000000084 [Rhino.RhinoDoc]>
this is under Rhino Commons.   Rhino--->RHinoDoc


Rhino.RhinoObject.Select(True, True, True, False, True, False)

"""
