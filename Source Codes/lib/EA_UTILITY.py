print "EA_UTILITY loaded"
import rhinoscriptsyntax as rs
import EA_FORMS as FORMS

def test():
    print "in func"

def print_list(list):
    temp = ""
    for x in list:
        temp += str(x) + "\n"
    rs.TextOut(message = temp)

def add_alias_set():
    rs.AddAlias("IL", '! _-RunPythonScript "L:\\4b_Applied Computing\\03_Rhino\\12_EnneadTab for Rhino\Source Codes\Selection\isolate_layer_by_selection.py"')
    rs.AddAlias("IB", '! _-RunPythonScript "L:\\4b_Applied Computing\\03_Rhino\\12_EnneadTab for Rhino\Source Codes\Selection\isolate similar block.py"')

def get_center(obj):
    corners = rs.BoundingBox(obj)
    min = corners[0]
    max = corners[6]
    center = (min + max)/2
    return center

def select_from_list(options,
                    title = "EnneadTab",
                    message = "test message",
                    muti_select = True,
                    button_names = ["Run Me"],
                    width = 500,
                    height = 500):


    return FORMS.ShowDocLayerSelectionDialog(options,
                                            title,
                                            message,
                                            muti_select,
                                            button_names,
                                            width,
                                            height)
