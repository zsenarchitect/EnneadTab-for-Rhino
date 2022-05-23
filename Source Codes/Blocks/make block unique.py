import rhinoscriptsyntax as rs


def get_center(obj):
    corners = rs.BoundingBox(obj)
    min = corners[0]
    max = corners[6]
    center = (min + max)/2
    return center

def make_block_unique():

    will_explode_nesting = rs.ListBox(items = [True, False], message =  "Explode nesting block?", title = "Make Block Unique", default = None)

    rs.EnableRedraw(False)
    orginal_blocks = rs.GetObject("Select block instance to make unique", filter = 4096, preselect = True)
    map(lambda x: make_unique(x, will_explode_nesting), [orginal_blocks])

def make_unique(orginal_block, will_explode_nesting):
    transform = rs.BlockInstanceXform(orginal_block)
    old_block_name = rs.BlockInstanceName(orginal_block)

    new_block_name = old_block_name + "_new"
    while True:
        new_block_name += "_new"
        print new_block_name
        #if rs.IsBlockInUse(new_block_name, where_to_look = 0):
        if new_block_name not in rs.BlockNames():
            break


    temp_block = rs.InsertBlock(old_block_name, (0,0,0))
    bounding_box_center = get_center(temp_block)
    temp_objs = rs.ExplodeBlockInstance(temp_block, explode_nested_instances = will_explode_nesting)
    dot_text = new_block_name
    dot = rs.AddTextDot(dot_text, bounding_box_center)
    block_contents = list(temp_objs)
    block_contents.append(dot)
    new_block = rs.AddBlock(block_contents, (0,0,0), name = new_block_name, delete_input = True)

    rs.InsertBlock2(new_block_name, transform)
    rs.DeleteObject(orginal_block)
    #rs.Command("!_ReplaceBlock  SelectFromBlockDefinitionList -Enter  \"{}\"".format(new_block_name))
    # rs.Command("_BlockEdit")_SelectFromBlockDefinitionList



if __name__ == "__main__":
    make_block_unique()
