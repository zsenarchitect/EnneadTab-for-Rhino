import rhinoscriptsyntax as rs



def isolate_block():



    rs.EnableRedraw(False)
    orginal_blocks = rs.GetObjects("Select block instances to isolate", filter = 4096, preselect = True)
    block_names = [rs.BlockInstanceName(x) for x in orginal_blocks]
    
    block_collection = []
    for block_name in block_names:
        block_collection.extend(rs.BlockInstances(block_name))

    rs.UnselectAllObjects()
    rs.SelectObjects( block_collection)
    invert_objs = rs.InvertSelectedObjects(include_lights = True, include_grips = True, include_references = True)
    rs.HideObjects(invert_objs)


    #rs.Command("Isolate")



if __name__ == "__main__":
    isolate_block()
