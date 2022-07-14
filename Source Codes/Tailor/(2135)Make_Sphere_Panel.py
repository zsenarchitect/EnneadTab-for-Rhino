import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc
import time
import sys
sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib')
import EA_UTILITY as EA


def process_srf(srf):
    pass
    back_layer = rs.OffsetSurface(srf, -20)
    outter_layer = rs.OffsetSurface(srf, 20)
    back_solid = rs.OffsetSurface(back_layer, -180, create_solid = True)



    border = rs.DuplicateSurfaceBorder(srf, type = 0)
    #pipe = rs.AddPipe(border, 0, 10)
    rs.UnselectAllObjects()
    rs.SelectObjects([srf, border])

    #border = rs.JoinCurves(rs.ExplodeCurves(border), delete_input = True)

    rs.Command("OffsetCrvOnSrf  10 _enter")
    rs.UnselectAllObjects()
    offseted_border = rs.LastCreatedObjects()
    rs.SelectObject(srf)
    #rs.Command("split _enter")
    #return

    projected_offset_crv = rs.PullCurve(back_layer, offseted_border)
    if len(projected_offset_crv) != 1:
        projected_offset_crv = rs.JoinCurves(projected_offset_crv, delete_input = True)
    projected_offset_crv2 = rs.PullCurve(outter_layer, offseted_border)
    if len(projected_offset_crv2) != 1:
        projected_offset_crv2 = rs.JoinCurves(projected_offset_crv2, delete_input = True)
    rs.DeleteObject(back_layer)
    rs.DeleteObject(outter_layer)
    extruded_cut = rs.AddLoftSrf((projected_offset_crv, projected_offset_crv2))
    print extruded_cut

    cuts = rs.SplitBrep(srf, extruded_cut, delete_input = False)
    cuts.sort(key = lambda x: rs.Area(x))
    true_shape = cuts[1]
    rs.DeleteObject(cuts[0])
    rs.DeleteObject(extruded_cut)
    rs.DeleteObjects([projected_offset_crv, projected_offset_crv2, offseted_border, border])

    outter_panel = rs.OffsetSurface(true_shape, -50, create_solid = True)
    rs.DeleteObject(true_shape)
    final = rs.BooleanUnion([outter_panel, back_solid])
    rs.ShrinkTrimmedSurface(final)
    return final

    #offset_crv = rs.OffsetCurveOnSurface(border, srf, 10)



def Run():

    srfs = rs.GetObjects("get base srfs", preselect = True)
    print srfs

    start = time.time()
    rs.EnableRedraw(False)
    collection = []
    map(lambda x: collection.append(process_srf(x)), srfs)

    group = rs.AddGroup()
    rs.AddObjectsToGroup(collection, group)


    end = time.time()
    used_time = end - start
    rs.MessageBox("time used = {} seconds = {}mins".format(used_time, used_time/60))




######################  main code below   #########
if __name__ == "__main__":

    Run()


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
