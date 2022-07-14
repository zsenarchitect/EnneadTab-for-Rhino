import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc
import math


import sys
sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib')
import EA_UTILITY as EA

"""
selected_block = rs.GetObject()
print rs.BlockInstanceXform(selected_block)
"""

def make_stair_block_from_pts():
    """
    goal: user pick starting pt and ending pt, tool calcuate the horitiontal and vertical distance, divide steps by max riser. Make stair block and insert at user pick location.

    note: Create polysurf by extruding guide crvs, which was curve union by arraying step curve profile.
    """
    pass

    #user pick starting pt and end pt
    start_pt = rs.GetPoint(message = "Pick starting pt for stair")
    end_pt = rs.GetPoint(message = "Pick ending pt for stair")

    #user enter max riser height and width
    max_riser, stair_width = EA.get_sticky("MAX_RISER", 170), EA.get_sticky("STAIR_RISER", 2000)
    max_riser, stair_width = rs.PropertyListBox(items = ["Max riser height(file unit)", "Run Width(file unit)"], values = [max_riser, stair_width], message = "Enter stair primitive data", title = "Stair Maker")
    #max_riser = rs.RealBox(message = "Max riser height number", default_number = 170, title = "EnneadTab")
    max_riser, stair_width = float(max_riser), float(stair_width)
    EA.set_sticky("MAX_RISER", max_riser)
    EA.set_sticky("STAIR_RISER", stair_width)
    print max_riser
    rs.EnableRedraw(False)


    #calcuate steps riser and thread by vectical dist/max riser height, horitiontal dist/ step count
    vertical_diff = end_pt[2] - start_pt[2]
    x0 = [start_pt[0], start_pt[1], 0]
    x1 = [end_pt[0], end_pt[1], 0]

    local_x = rs.VectorCreate(x1, x0)
    local_y = rs.VectorRotate(local_x, 90, [0,0,1])
    horitiontal_diff = rs.Distance(x0, x1)
    print vertical_diff
    print horitiontal_diff
    num_of_step = int(math.ceil(vertical_diff / max_riser))
    actual_riser = vertical_diff / num_of_step
    actual_thread = horitiontal_diff / num_of_step
    print num_of_step, actual_riser, actual_thread

    #create step profile pts list by step riser and thred depth
    step_overlap = 2 * actual_thread
    x0 = [0,0,0]
    x1 = [actual_thread + step_overlap, 0,0]
    x2 = [actual_thread + step_overlap, 0, -actual_riser]
    x3 = [0, 0, -actual_riser]
    pts = [x0, x1, x2, x3]
    pts.append(x0)
    profile = rs.AddPolyline(pts)
    profile_collection = [profile]


    #array those step profile and curve boolean
    direction = rs.VectorCreate([actual_thread, 0, actual_riser], x0)
    for i in range(num_of_step):
        profile = rs.CopyObject(profile, direction)
        profile_collection.append(profile)

    #curve boolean to get slope soffit of satir
    union_profile = rs.CurveBooleanUnion(profile_collection)
    trimmer_crv_pts = []
    insert_pt = rs.MoveObject(rs.AddPoint(x1), [-actual_thread,0,0])
    trimmer_crv_pts.append(rs.CopyObject(insert_pt , direction * (-1)))
    trimmer_crv_pts.append(rs.CopyObject(trimmer_crv_pts[-1] , direction * (i+1)))
    trimmer_crv_pts.append(rs.CopyObject(trimmer_crv_pts[-1] , [5000,0,0]))
    trimmer_crv_pts.append(rs.CopyObject(trimmer_crv_pts[0] , [5000,0,0]))
    trimmer_crv_pts.append(trimmer_crv_pts[0])
    trimmer_crv = rs.AddPolyline(trimmer_crv_pts)
    final_profile = rs.CurveBooleanDifference(union_profile, trimmer_crv)
    rs.DeleteObjects(profile_collection)
    rs.DeleteObjects(trimmer_crv_pts)
    rs.DeleteObjects(trimmer_crv)
    rs.DeleteObject(insert_pt)
    rs.DeleteObject(union_profile)

    #extrude width, and cap
    stair_mass = rs.ExtrudeCurveStraight(final_profile, x0, [0, stair_width, 0])
    rs.DeleteObjects(final_profile)
    rs.CapPlanarHoles(stair_mass)

    #make a block, inclucde dot text for name.
    block_contents = [stair_mass]
    stair_name = "EA_stair"
    all_block_names = rs.BlockNames()
    while True:
        if stair_name not in all_block_names:
            break
        stair_name += "_new"
    rs.AddBlock(block_contents, base_point = x0, name = stair_name, delete_input = True)


    #insert block back at user pick pts
    initial_plane = rs.CreatePlane([0,0,0], x_axis = [1,0,0], y_axis = [0,1,0], ignored = None)
    final_plane = rs.CreatePlane(start_pt, x_axis = local_x, y_axis = local_y, ignored = None)
    print initial_plane
    print final_plane
    transform = rs.XformChangeBasis(final_plane,initial_plane)
    #print transform
    #rs.InsertBlock2(stair_name, transform)
    temp_block = rs.InsertBlock(stair_name, [0,0,0])
    rs.TransformObject(temp_block, transform)




######################  main code below   #########
if __name__ == "__main__":

    make_stair_block_from_pts()


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


res = rs.StringBox(message = "type in text", default_value = "default", title = "using stringbox")
print res

res = rs.GetString(message = "type in text or click options", strings = ["opt_1", "opt_2", "opt_3"])
print res

res = rs.EditBox(message = "type in text", default_string = "default string", title = "edit box")
print res


rs.TextOut(message = "text to display\nLine 1\nLine 2", title = "my title")


rs.MessageBox(message = "text to display", buttons= 4 | 48, title = "message box")

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
