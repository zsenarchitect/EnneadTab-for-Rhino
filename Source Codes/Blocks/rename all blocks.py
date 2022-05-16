import rhinoscriptsyntax as rs
from scriptcontext import doc
import Rhino

def Rename(blockName):
#    blockName = rs.GetString("block to rename")
    instanceDefinition = doc.InstanceDefinitions.Find(blockName, True)
    if not instanceDefinition:
        print "{0} block does not exist".format(blockName)
        return

    newName = doc_name + "_" + blockName
    instanceDefinition = doc.InstanceDefinitions.Find(newName, True)
    if instanceDefinition:
        print "the name '{0}' is already taken by another block".format(newName)
        return


    data = "{}  -->  {}".format(blockName, newName)
    log.append( data )
    rs.RenameBlock(blockName, newName)

if __name__ == "__main__":

    try:
        doc_name = doc.Name.split(".3dm")[0]
    except:
        doc_name = "Untitled"

    log = ["[{}] will be prefix to all blocks".format(doc_name)]

    block_names = rs.BlockNames()

    for name in block_names:
#        print name
        Rename(name)


    if len(log) > 0:

        log = "\n".join(log)
        rs.TextOut(message = log, title = "map of new names")
    else:
        Rhino.UI.Dialogs.ShowMessage("No block changed", title = "it is good!")
