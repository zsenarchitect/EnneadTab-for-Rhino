import rhinoscriptsyntax as rs
from scriptcontext import doc
import Rhino

def get_center(obj):
    corners = rs.BoundingBox(obj)
    min = corners[0]
    max = corners[6]
    center = (min + max)/2
    return center



def display_block_name():


    blocks = rs.ObjectsByType(4096, select = False, state = 0)

    bounding_box_centers = [get_center(x) for x in blocks]
    dot_texts = [ rs.BlockInstanceName(x) for x in blocks]
    dots = [rs.AddTextDot(text,pt) for text, pt in zip(dot_texts,bounding_box_centers)]
    group_name = "block_names_display_dots"
    rs.AddGroup(group_name = group_name)
    rs.AddObjectsToGroup(dots, group_name)


def summery_of_block_usage():
    block_names = rs.BlockNames(sort = False)
    OUT = ""
    for block_name in block_names:
        OUT += "\n[{}] status:".format(block_name)
        top_level_count = rs.BlockInstanceCount(block_name, where_to_look = 0)
        OUT += "\nIt has {} counts as top level block".format(rs.BlockInstanceCount(block_name,where_to_look = 0))
        OUT += "\nIt has {} counts in nested block".format(rs.BlockInstanceCount(block_name,where_to_look = 1) - top_level_count)
        OUT += "\nIt has {} counts in block definition type".format(rs.BlockInstanceCount(block_name,where_to_look = 2))

        upper_blocks = rs.BlockContainers(block_name)
        if len(upper_blocks) != 0:
            OUT += "\nIt has {} upper level blocks as below".format(len(upper_blocks))
            for item in upper_blocks:
                OUT += "\n\t\t[{}]".format(item)

        block_definition = doc.InstanceDefinitions.Find(block_name)
        objs = block_definition.GetObjects()
        inner_blocks = filter(lambda x: rs.IsBlockInstance(x), objs)
        inner_blocks.sort(key = lambda x: rs.BlockInstanceName(x))
        if len(inner_blocks) != 0:
            OUT += "\nIt has {} nesting blocks as below".format(len(inner_blocks))
            for item in inner_blocks:
                OUT += "\n\t\t[{}]".format(rs.BlockInstanceName(item))


        OUT += "\n"

    rs.TextOut(message = OUT, title = "Summery")


if __name__ == "__main__":



    display_block_name()
    summery_of_block_usage()
