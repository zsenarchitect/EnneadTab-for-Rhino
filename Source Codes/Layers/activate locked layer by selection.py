#import Rhino
import rhinoscriptsyntax as rs
#import scriptcontext as sc

import sys
sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib')
sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\Selection')
import EA_UTILITY as EA
import inspect_locked_layer


def Run():
    locked_layers, open_layers = inspect_locked_layer.get_force_selected_layer()
    for layer in locked_layers:
        rs.LayerLocked(layer, locked = False)
        set_parent_layer_unlock(layer)


def set_parent_layer_unlock(layer):
    parent_layer = rs.ParentLayer(layer)
    if parent_layer is None:
        return
    rs.LayerLocked(parent_layer, locked = False)
    set_parent_layer_unlock(parent_layer)


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
