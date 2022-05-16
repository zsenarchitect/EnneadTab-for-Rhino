import rhinoscriptsyntax as rs
from scriptcontext import doc
import Rhino

def Rename(blockName):
#    blockName = rs.GetString("block to rename")
    if keyword not in blockName:
        return
    instanceDefinition = doc.InstanceDefinitions.Find(blockName, True)
    if not instanceDefinition:
        print "{0} block does not exist".format(blockName)
        return





    newName =  blockName.replace(keyword , replacement_text)
    while True:

        try:
            instanceDefinition = doc.InstanceDefinitions.Find(newName, True)
            break
        except:
            newName += "_"



    data = "{}  -->  {}".format(blockName, newName)
    log.append( data )
    rs.RenameBlock(blockName, newName)

if __name__ == "__main__":
    log = []

    keyword = rs.StringBox(message = "type in keyword to search in name", default_value = "keyword text to remove from blocks names", title = "rename block names")
    replacement_text = rs.StringBox(message = "type in text, you can type '#empty'(yes hashtag, no quote) as a way to remove previous keyword.", default_value = "replacement text to replace previous keyword", title = "rename block names")
    if replacement_text == "#empty":
        replacement_text = ""

    """
    gs = Rhino.Input.Custom.GetString()
    gs.SetCommandPrompt("Name of surffix to remove")
    gs.SetDefaultString("<- revit view name>")
    gs.AcceptNothing(False)
    gs.GetLiteralString()

    if gs.CommandResult()!=Rhino.Commands.Result.Success:
#        return gs.CommandResult()
        pass

    keyword = gs.StringResult().Trim()
#    keyword = "-NoSheet-3D-Facade Fins only _MF__from_michael_fierle_"
    """


    block_names = rs.BlockNames()

    for name in block_names:
        # print name
        Rename(name)


    if len(log) > 0:

        log = "\n".join(log)
        rs.TextOut(message = log, title = "here are the changed block names")
    else:
        Rhino.UI.Dialogs.ShowMessage("No block changed", title = "it is good!")
