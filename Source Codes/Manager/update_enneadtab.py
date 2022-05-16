import rhinoscriptsyntax as rs
import scriptcontext as sc
import shutil

def get_latest_toolbar():

    # rs.CloseToolbarCollection("Enscape.Rhino7.Plugin", prompt = False)
    rs.CloseToolbarCollection("EnneadTab", prompt = False)
    original = r"L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Working\EnneadTab.rui"
    target = r"L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\EnneadTab for Rhino\EnneadTab.rui"

    shutil.copyfile(original, target)
    rs.OpenToolbarCollection(target)

    rs.MessageBox(message = "Latest EnneadTab Loaded".format(res), buttons= 0 | 48, title = "EA monitor")






##########################################################################

if( __name__ == "__main__" ):

  get_latest_toolbar()
