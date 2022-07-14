import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

import sys
sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib')
import EA_UTILITY as EA



def Run():

    EA.test()
    EA.toast(message = "123", title = "my big title")
    #EA.print_list([1,2,3,4,5,6,7,8,9])
    #res = EA.select_from_list(["a","c","apple", 1],muti_select = True)
    #EA.print_list(res)





######################  main code below   #########
if __name__ == "__main__":
    rs.EnableRedraw(False)
    Run()


"""
##The Search Paths options manage locations to search for bitmaps that used for render texture and bump maps.
rs.AddSearchPath(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib\EA_UTILITY.py')


import imp
ref_module = imp.load_source("sync_queue_monitor", r'L:\\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\Revit\sync_queue_monitor.py')

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
