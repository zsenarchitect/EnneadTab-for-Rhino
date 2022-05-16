import rhinoscriptsyntax as rs
import scriptcontext as sc
import random


def get_sticky(sticky_name, default_value_if_no_sticky):
    if sc.sticky.has_key(sticky_name):
        return sc.sticky[sticky_name]
    else:
        return default_value_if_no_sticky

def set_sticky(sticky_name, value_to_write):
    sc.sticky[sticky_name] = value_to_write
    

def random_block():

    Ids = rs.GetObjects("Select block instances to rotate", filter = 4096, preselect=True)




        
    default_use_rotation = get_sticky("random_transform_rotation", True)
    default_use_scale_1d_soft = get_sticky("random_transform_scale_1d_soft", True)
    default_use_scale_1d_taller = get_sticky("random_transform_scale_1d_taller", False)
    

    option_list = [["Rotation", default_use_rotation], ["Height scale 1D softly(0.9~1.1 factor)", default_use_scale_1d_soft], ["Height scale 1D taller(1.4~1.7 factor)(override softer option if checked)", default_use_scale_1d_taller]]
    res = rs.CheckListBox(items = option_list,
                            message= "select random options from below",
                            title="EnneadTab Random Transform")
    print res
    for option, state in res:
        if option == option_list[0][0]:
            use_rotation = state
            continue
        if option == option_list[1][0]:
            use_1d_H = state
            continue
        if option == option_list[2][0]:
            use_1d_H_tall = state
            continue


    if Ids is None: return
    vec = rs.VectorCreate([0,0,1], [0,0,0])


    for Id in Ids:
        pt = rs.BlockInstanceInsertPoint(Id)
        if use_rotation:
            ang = random.randrange(-180, 180)
            rs.RotateObject(Id, pt,ang,vec)

        if use_1d_H:
            z_scale = random.uniform(0.9, 1.1)
        else:
            z_scale = 1.0


        if use_1d_H_tall:
            z_scale = random.uniform(1.4, 1.7)


        if z_scale != 1.0:
            rs.ScaleObject(Id, pt,[1,1,z_scale],False)


    # sc.sticky["random_transform_rotation"] = use_rotation
    set_sticky("random_transform_rotation", use_rotation)
    set_sticky("random_transform_scale_1d_soft", use_1d_H)
    set_sticky("random_transform_scale_1d_taller", use_1d_H_tall)
    

    
if __name__ == "__main__":
    random_block()
