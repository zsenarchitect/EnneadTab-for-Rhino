#!/usr/bin/python
# -*- coding: utf-8 -*-

print "EA_UTILITY loaded"
import rhinoscriptsyntax as rs
import scriptcontext as sc

"""
math and misc
"""
def has_any_keyword(input, keywords):
    for keyword in keywords:
        if keyword in input.lower():
            return True
    return False


def test():
    print "in func"


def print_list(list):
    temp = ""
    for x in list:
        temp += str(x) + "\n"
    rs.TextOut(message = temp)


def map_num_linear(X, x0, x1, y0, y1):
    """
    x0, x1 ---> input range
    y0, y1 ---> output range
    """
    k = (y1 - y0) / (x1 - x0)
    b = y0 - k * x0
    #print k
    #print b
    Y = k * float(X) + b
    return Y


def map_num_with_clamp(X, x0, x1, y0, y1, clamp0, clamp1):
    """
    if clamp0 < x0 or clamp1 > x1:
        #raise ClampError('clamps must be between input range')
        print "clamp error"
        return None
    """
    """
    X = max(X, clamp0)
    X = min(X, clamp1)
    """
    if X < clamp0:
        return y0
    if X > clamp1:
        return y1
    return map_num_linear(X, clamp0, clamp1, y0, y1)


def filter_by_mask(X, Y):
    """
    X ---> obj list
    Y ---> boolean list
    """
    OUT = []
    for a, b in zip(X, Y):
        if b:
            OUT.append(a)
    return OUT


"""
export and reading, stickys
"""
def read_txt_as_list(filepath = "path", use_encode = False):
    if use_encode:
        import io
        with io.open(filepath, encoding = "utf8") as f:
            lines = f.readlines()
    else:
        with open(filepath) as f: #encoding = "utf8"
            lines = f.readlines()
    return map(lambda x: x.replace("\n",""), lines)


def save_list_to_txt(list, filepath, end_with_new_line = False):
    with open(filepath, 'w') as f:
        # f.writelines(list)
        f.write('\n'.join(list))
        if end_with_new_line:
            f.write("\n")


def read_file_safely(original_path, file_name = None):
    #print original_path
    if file_name is None:
        file_name = original_path.rsplit("\\", 1)[1]
    local_folder = get_EA_setting_folder() + "\\" + "Local Copy Dump"
    local_folder = secure_folder(local_folder)
    local_path = "{}\{}".format(local_folder, file_name)
    import shutil
    shutil.copyfile(original_path, local_path)
    #print "###"
    #print local_path
    content = read_txt_as_list(local_path)
    return content

def read_data_from_excel(filepath, worksheet = "Sheet1", by_line = True):
    import sys
    reload(sys)
    # 设定了输出的环境为utf8
    sys.setdefaultencoding('utf-8')
    import sys
    sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Dependency Modules')

    import xlrd
    wb = xlrd.open_workbook(filepath)#, encoding_override = "cp1252")#""big5")#"iso2022_jp_2")#"gb18030")#"gbk")#"hz")  #"gb2312")   #"utf8"
    sheet = wb.sheet_by_name(worksheet)
    #print sheet.cell_value(2, 1)
    OUT = []

    for i in range(0, sheet.nrows):
        OUT.append(sheet.row_values(i))
    return OUT


def get_sticky(sticky_name, default_value_if_no_sticky):
    if sc.sticky.has_key(sticky_name):
        return sc.sticky[sticky_name]
    else:
        return default_value_if_no_sticky


def set_sticky(sticky_name, value_to_write):
    sc.sticky[sticky_name] = value_to_write


def get_sticky_longterm(sticky_name, default_value_if_no_sticky):
    folder = get_EA_setting_folder() + "\Longterm Sticky"
    #print folder
    folder = secure_folder(folder)
    file = folder + "\\" + sticky_name + ".STICKY"
    #print file
    #print sticky_name
    #print "***"
    #print get_filenames_in_folder(folder)
    if sticky_name + ".STICKY" not in get_filenames_in_folder(folder):
        print "stickyname not found in folder"
        set_sticky_longterm(sticky_name, default_value_if_no_sticky)
        return default_value_if_no_sticky
    content = read_txt_as_list(file)
    #print "****"
    #print value
    if content is None or len(content) == 0:
        set_sticky_longterm(sticky_name, default_value_if_no_sticky)
        return default_value_if_no_sticky
    else:
        if len(content) == 1:
            set_sticky_longterm(sticky_name, content[0])
            return content[0]
        value, type = content
        if type == "float":
            value = float(value)
        if type == "int":
            value = int(value)
        return value


def set_sticky_longterm(sticky_name, value_to_write):
    type = "string"
    if isinstance(value_to_write, float):
        type = "float"
    if isinstance(value_to_write, int):
        type = "int"
    folder = get_EA_setting_folder() + "\Longterm Sticky"
    folder = secure_folder(folder)
    file = folder + "\\" + sticky_name + ".STICKY"
    save_list_to_txt([value_to_write, type], file)


"""
folder manipulation
"""
def get_filenames_in_folder(folder):
    import os
    #print "&&&&&&"
    #print os.listdir(folder)
    return os.listdir(folder)


def get_user_folder():
    import os
    return "{}\Documents".format(os.environ["USERPROFILE"])

def is_SZ():
    import os
    #print os.environ["USERPROFILE"]
    if os.environ["USERPROFILE"] == r"C:\Users\szhang":
        return True
    return False


def get_EA_setting_folder():
    folder = get_user_folder() + "\EnneadTab Settings"
    #print folder
    return secure_folder(folder)


def get_special_folder_in_EA_setting(folder_name):
    folder = get_EA_setting_folder() + "\{}".format(folder_name)
    return secure_folder(folder)


def secure_folder(path):
    import os
    try:
        os.makedirs(path)

    except Exception as e:

        print "folder cannot be secured"
        print e
        pass
    return path


"""
UI
"""
def rhino_layer_to_user_layer(name):
    return "[{}]".format(name.replace("::", "] - ["))


def user_layer_to_rhino_layer(name):
    return name[1:-1].replace("] - [", "::")


def select_from_list(options,
                    title = "EnneadTab",
                    message = "test message",
                    muti_select = True,
                    button_names = ["Run Me"],
                    width = 500,
                    height = 500):

    import EA_FORMS as FORMS
    return FORMS.ShowDocLayerSelectionDialog(options,
                                            title,
                                            message,
                                            muti_select,
                                            button_names,
                                            width,
                                            height)


def toast(message = "Placeholder text",
        title = "Some title text",
        app_name = "EnneadTab For Rhino",
        icon = None, click = None, actions = None):
    import EA_TOASTER
    EA_TOASTER.toast(message, title, app_name, icon, click, actions)


"""
rhino operation
"""
def add_alias_set():
    rs.AddAlias("IL", '! _-RunPythonScript "L:\\4b_Applied Computing\\03_Rhino\\12_EnneadTab for Rhino\Source Codes\Selection\isolate_layer_by_selection.py"')
    rs.AddAlias("IB", '! _-RunPythonScript "L:\\4b_Applied Computing\\03_Rhino\\12_EnneadTab for Rhino\Source Codes\Selection\isolate similar block.py"')
    rs.AddAlias("IF", '! _-RunPythonScript "L:\\4b_Applied Computing\\03_Rhino\\12_EnneadTab for Rhino\Source Codes\Selection\isolate_family_layer.py"')
    rs.AddAlias("GetLatestEnneadTab", '! _-RunPythonScript "L:\\4b_Applied Computing\\03_Rhino\\12_EnneadTab for Rhino\Source Codes\Manager\update_enneadtab.py"')
    rs.AddAlias("RandomizeBlock", '! _-RunPythonScript "L:\\4b_Applied Computing\\03_Rhino\\12_EnneadTab for Rhino\Source Codes\Blocks\\random transform.py"')
    rs.AddAlias("RandomlyDeSelectBlock", '! _-RunPythonScript "L:\\4b_Applied Computing\\03_Rhino\\12_EnneadTab for Rhino\Source Codes\Selection\UnselectRandom.py"')
    try:
        rs.DeleteAlias("RandomllyDeSelectBlock")
    except:
        print "not found"
        pass


def set_text_justifiction(text_id, justification):
    """
    1 = Left
    2 = Center (horizontal)
    4 = Right
    65536 = Bottom
    131072 = Middle (vertical)
    262144 = Top
    """

    import System
    import Rhino
    #set new justification like with rs.AddText
    new_justification  = System.Enum.ToObject(Rhino.Geometry.TextJustification, justification)

    #grab geometry of the text object
    text_geometry = rs.coercegeometry(text_id)
    text_geometry.Justification = new_justification

    #replace geometry of the rhino object with new justification geometry
    sc.doc.Objects.Replace(text_id,text_geometry)

def get_center(obj):
    corners = rs.BoundingBox(obj)
    min = corners[0]
    max = corners[6]
    center = (min + max)/2
    return center


def get_material_by_name(name):
    mats = sc.doc.Materials
    """
    for mat in mats:
        print mat.Name
    """



    mat = filter(lambda x: x.Name == name, mats)
    if len(mat) != 0:
        return mat[0]
    return None


def create_material(name, RGBAR, return_index = False):
    # RGBAR = (r,g,b,t,R)
    from System.Drawing import Color
    import Rhino
    material = Rhino.DocObjects.Material()
    material.Name = name
    material = Rhino.Render.RenderMaterial.CreateBasicMaterial(material, sc.doc)
    sc.doc.RenderMaterials.Add(material)


    sphere = Rhino.Geometry.Sphere(Rhino.Geometry.Plane.WorldXY, 500)
    id = sc.doc.Objects.AddSphere(sphere)
    obj = sc.doc.Objects.FindId(id)
    obj.RenderMaterial = material;
    obj.CommitChanges()

    material = get_material_by_name(name)
    if material is None:
        rs.TextOut(message = "No material found after creating material, contact Sen for help on why.", title = "EnneadTab")
    #material.CommitChanges()
    #print "begin changing material = {}".format(material)
    red, green, blue, transparency, reflectivity = RGBAR # trnasparency 0 = solid, 1 = see-thru,,,,,reflectivity 0 = matte, 255 = glossy
    material.DiffuseColor = Color.FromArgb(red,green,blue)
    #print material.DiffuseColor
    material.Transparency = transparency
    material.TransparentColor = Color.FromArgb(red,green,blue)
    #print material.TransparentColor
    material.ReflectionColor = Color.FromArgb(red,green,blue)
    material.Reflectivity = reflectivity
    material.ReflectionGlossiness = reflectivity
    material.Shine = reflectivity
    material.SpecularColor = Color.FromArgb(red,green,blue)
    material.AmbientColor  = Color.FromArgb(red,green,blue)

    material.CommitChanges()
    #rs.DeleteObject(id)
    if return_index:
        return material.MaterialIndex, id
    else:
        return material, id#return the sample material ball so the material is visible to search. you can delete ball with this ID after script.



#################### test area ###############
if( __name__ == "__main__" ):
    print create_material("test01", (32,108,134,0.95,250))
