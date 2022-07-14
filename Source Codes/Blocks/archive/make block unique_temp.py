import rhinoscriptsyntax as rs


def get_center(obj):
    corners = rs.BoundingBox(obj)
    min = corners[0]
    max = corners[6]
    center = (min + max)/2
    return center

def make_block_unique():

    will_explode_nesting = rs.ListBox(items = [True, False], message =  "Explode nesting block?", title = "Make Block Unique", default = None)


    original_blocks = rs.GetObjects("Select block instances to make unique", filter = 4096, preselect = True)
    selected_block_names = list(set([rs.BlockInstanceName(x) for x in original_blocks]))
    if len(selected_block_names) != 1:
        rs.MessageBox("Need to select single block, or a few block of same defination.")
        return
    rs.EnableRedraw(False)
    new_block_name = create_unique_block(original_blocks[0], will_explode_nesting)
    map(lambda x:replace_original_blocks(new_block_name, x), original_blocks)


def create_unique_block(orginal_block, will_explode_nesting):
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
    return new_block_name



def replace_original_blocks(new_block_name, original_block):
    transform = rs.BlockInstanceXform(original_block)
    rs.InsertBlock2(new_block_name, transform)
    rs.DeleteObject(original_block)


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
