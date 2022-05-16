import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def make_sample_blocks():


    #get curve
    base_crv = rs.GetObject(message = "pick base crv, prefer counter-clockwise direction", filter = rs.filter.curve, preselect = True)

    # add block to doc, here use propety box
    res = rs.PropertyListBox(items = ["Width", "Depth", "Height"], values = [1500, 200, 4500], message = "Enter sample block dimension similar to your spacing", title = "EnneadTab")
    print res
    #\nThis should best approximate the division to be used on facade layout.\n\tWidth = horitiontal division spacing\n\tDepth = from FOG to back of mullion\n\tHeight = vertical division spacving

    W, D, H = [float(x) for x in res]

    block_name = "EA_layout block_{} x {} x {}".format(W, D, H)
    block_name, insert_pt, ref_pt = create_block(block_name, W, D, H)
    temp_block = rs.InsertBlock(block_name, insert_pt)
    block_reference = [insert_pt, ref_pt]

    crv_segs = rs.ExplodeCurves(base_crv)

    collection = []
    print crv_segs
    for seg in crv_segs:
        count = rs.CurveLength(seg) / W
        pts_on_seg = rs.DivideCurve(seg, count, create_points = False)
        rs.DeleteObject(seg)
        for i in range(len(pts_on_seg) - 1):
            x0 = pts_on_seg[i]
            print x0
            x1 = pts_on_seg[i + 1]
            target_reference = [x0, x1]
            collection.append(rs.OrientObject( temp_block, block_reference, target_reference, flags = 3))



    rs.DeleteObject(temp_block)
    rs.EnableRedraw(enable = False)
    map(lambda x: set_vertical_scale(x, H), collection)
    group_name = block_name
    rs.AddGroup(group_name = block_name)
    rs.AddObjectsToGroup(collection, group_name)




def set_vertical_scale(block_instance, prefered_H):
    box_corners = rs.BoundingBox(block_instance)
    current_H = box_corners[7][2] - box_corners[0][2]
    scale_factor = prefered_H /current_H
    rs.ScaleObject( block_instance, rs.BlockInstanceInsertPoint(block_instance), (1,1,scale_factor) )



def create_block(name, W, D, H):

    pt0 = [0,0,0]
    pt1 = [W, D, H]
    pts = [pt0, pt1]
    ref_pt_coord = [W, 0, 0]

    box_corners = rs.BoundingBox(pts)
    box = rs.AddBox(box_corners)
    insert_pt = rs.AddPoint(pt0)
    ref_pt = rs.AddPoint(ref_pt_coord)
    block_contents = [box, insert_pt, ref_pt]
    block_name = rs.AddBlock(block_contents, insert_pt, name = name, delete_input = True)
    return block_name, pt0, ref_pt_coord


if __name__ == "__main__":
    make_sample_blocks()
