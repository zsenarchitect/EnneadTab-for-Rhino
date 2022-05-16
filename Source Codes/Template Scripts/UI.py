import rhinoscriptsyntax as rs


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


##################################################
def print_list(list):
    temp = ""
    for x in list:
        temp += str(x) + "\n"
    rs.TextOut(message = temp)




"""
rhino read excel, and write
http://developer.rhino3d.com/guides/rhinoscript/reading-excel-files/


print sc.doc ---> <Rhino.RhinoDoc object at 0x0000000000000084 [Rhino.RhinoDoc]>
this is under Rhino Commons.   Rhino--->RHinoDoc
"""
