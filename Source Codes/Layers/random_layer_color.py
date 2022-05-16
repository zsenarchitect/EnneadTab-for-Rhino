import rhinoscriptsyntax as rs
import scriptcontext as sc
import random
from System.Drawing import Color
from colorsys import hsv_to_rgb, rgb_to_hsv

def random_layer_color():
    options = ["Desaturated Colors", "Full RGB"]
    color_options = rs.ListBox(items = options, message= "select color option from below, only uncolored layer(default black) will be modified.\n\nKeyword for hue suggestion.\n\t'glass' and 'water' as blue hue.\n\t'grass' as green hue.", title = "random layer color", default = options[0])
    if color_options == options[0]:
        use_desaturated_color = True
    else:
        use_desaturated_color = False




    all_layer_names = rs.LayerNames()
    for layer in all_layer_names:
        current_color = rs.LayerColor(layer)
        if str(current_color) == "Color [A=255, R=0, G=0, B=0]":
            rs.LayerColor(layer, color = random_color(layer, use_desaturated_color))

def random_color(layer_name, use_desaturated_color):



    layer_name = layer_name.lower()

    def reduce():
        return int(255*random.random() * 0.1)
    def strong():
        return int(50*random.random()) + 200

    if "glass" in layer_name:
        red = reduce()
        green = reduce()
        blue = strong()
    elif "grass" in layer_name:
        red = reduce()
        green = strong()
        blue = reduce()
    elif "water" in layer_name or "pool" in layer_name:
        red = reduce()
        green = reduce()
        blue = strong()
    else:
        red = int(255*random.random())
        green = int(255*random.random())
        blue = int(255*random.random())


    color =  Color.FromArgb(red,green,blue)
    if not use_desaturated_color:
        return color
    #return color

    normalized_color = (color[0]/256.0, color[1]/256.0, color[2]/256.0)
    hsv_color = rgb_to_hsv(*normalized_color)
    grayed_hsv_color = (hsv_color[0], 0.6, hsv_color[2])
    grayed_rgb_color = hsv_to_rgb(*grayed_hsv_color)
    denormalized_rgb_color = (int(grayed_rgb_color[0]*256), int(grayed_rgb_color[1]*256), int(grayed_rgb_color[2]*256))

    return denormalized_rgb_color

##########################################################################

if( __name__ == "__main__" ):

  random_layer_color()
