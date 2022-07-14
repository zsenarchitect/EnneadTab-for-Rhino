import rhinoscriptsyntax as rs
import os
from scriptcontext import doc


def export_by_layer(extension = "3dm"):



    target_main_folder = rs.BrowseForFolder( folder = None, message = "Select an output folder", title = "Select an output folder")

    try:
        doc_name = doc.Name.split(".3dm")[0]
    except:
        doc_name = "Untitled"
    EA_export_folder = "{}\EnneadTab Export By Layer from {}".format(target_main_folder, doc_name)
    if not os.path.exists(EA_export_folder):
        os.makedirs(EA_export_folder)

    

    """
    try this, before explode all block, make a copy of all block instances to a
    temp collection A, here the name does not matter anymore, explode all contents
    in the block to have it released to main file, keep a record of all newly
    leased objes as collection B.      Do export by layer but ignore blocks this time.    After
    export is done, delete all objs in colelction B.
    """
    block_collection = []
    all_block_names = rs.BlockNames( sort = False )
    for block_name in all_block_names:
        block = rs. BlockInstances(block_name)
        block_collection.extend(block)

    block_collection_trash = rs.CopyObjects(block_collection)
    trash_geo = []
    for block in block_collection_trash:
        trash_geo.extend(rs.ExplodeBlockInstance(block, explode_nested_instances = True))


    all_layers = rs.LayerNames()
    for layer in all_layers:
        rs.UnselectAllObjects()
        raw_objs = rs.ObjectsByLayer(layer, select = False)
        filter = rs.filter.instance
        objs = [obj for obj in raw_objs if rs.ObjectType(obj)!= filter]
        if len(objs) == 0:
            continue
        rs.SelectObjects(objs)
        filepath = "{}\{}.{}".format(EA_export_folder, layer.replace("::", "_"), extension)
        rs.Command("!_-Export \"{}\" -Enter -Enter".format(filepath))
    #rs.Command("!_Undo")


    rs.DeleteObjects(trash_geo)
    rs.MessageBox(message = "All layer processed", buttons= 0 | 48, title = "Export by Layer")



#####
if __name__ == "__main__":
    export_by_layer()
