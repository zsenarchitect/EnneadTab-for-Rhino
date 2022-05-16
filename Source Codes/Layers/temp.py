import rhinoscriptsyntax as rs
import scriptcontext as sc
from System.Drawing import Color


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
        scheme_layer_options = [["Glass", (0, 0, 250)],
                                ["Metal", (120, 140, 160)],
                                ["Mullion", (40 ,40, 40)],
                                ["Shadowbox", (10, 60, 80)]]
    elif new_layer_scheme_options == options[1]:
        parent_layer = "EA_Program"
        scheme_layer_options = ["Office",
                                "Retail",
                                "MEP",
                                "Resi"]
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

                    rs.AddLayer(name = "{}::{}".format(parent_layer,option),
                                color = get_color(color),
                                parent = None)
                    continue






##########################################################################

if( __name__ == "__main__" ):

  initiate_layers()
