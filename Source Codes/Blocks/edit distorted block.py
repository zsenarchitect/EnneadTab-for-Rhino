import rhinoscriptsyntax as rs




def edit_block():

    id = rs.GetObject("Select block instance to edit", filter = 4096, preselect = True)
    name = rs.BlockInstanceName(id)

    new_id = rs.InsertBlock(name, (0,0,0))

    rs.SelectObject(new_id)
    rs.ZoomSelected()
    # rs.Command("_BlockEdit")



if __name__ == "__main__":
    edit_block()
