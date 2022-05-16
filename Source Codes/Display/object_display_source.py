import rhinoscriptsyntax as rs
import scriptcontext as sc

def modify_disply_source():

    def change_objs_display(objs):
        if color_by_layer:
            rs.ObjectColorSource(objs, source = 0)
        if material_by_layer:
            rs.ObjectMaterialSource(objs, source = 0)


    def update_block_display(block_name):
        block_definition = sc.doc.InstanceDefinitions.Find(block_name)
        objs = block_definition.GetObjects()
        change_objs_display(objs)



    option_list = [["Make all object color defined by layer", True], ["Make all object material defined by layer", True]]
    res = rs.CheckListBox(items = option_list,
                            message= "This will also affect contents inside blocks",
                            title="EnneadTab")

    for option, state in res:
            if option == option_list[0][0]:
                color_by_layer = state
            if option == option_list[1][0]:
                material_by_layer = state

    # change for general obj display
    objs = rs.AllObjects()
    change_objs_display(objs)

    #change for objs inside blocks
    block_names = rs.BlockNames(sort = True)
    map(update_block_display, block_names)




if __name__ == "__main__":
    modify_disply_source()
