import rhinoscriptsyntax as rs



def select_similar_blocks():



    rs.EnableRedraw(False)
    orginal_blocks = rs.GetObjects("Select block instances to isolate", filter = 4096, preselect = True)
    block_names = [rs.BlockInstanceName(x) for x in orginal_blocks]

    block_collection = []
    for block_name in block_names:
        block_collection.extend(rs.BlockInstances(block_name))

    rs.UnselectAllObjects()
    rs.SelectObjects( block_collection)


if __name__ == "__main__":
    select_similar_blocks()
