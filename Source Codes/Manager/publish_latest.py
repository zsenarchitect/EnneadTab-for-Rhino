import rhinoscriptsyntax as rs
import scriptcontext as sc
import shutil

def publish_latest_toolbar():
    options = ["Exit without action", "Confirm"]
    res = rs.ListBox(items = options, message =  "Wait...Only proceed if your name is Sen Zhang", title = "STOP!", default = options[0])
    if res != options[1]:
        return

    res = rs.SaveToolbarCollection("EnneadTab")
    rs.MessageBox(message = "saving 'EnneadTab.rui' file = {}".format(res), buttons= 0 | 48, title = "EA monitor")

    original = r"L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Working\EnneadTab.rui"
    target = r"L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\EnneadTab for Rhino\EnneadTab.rui"

    shutil.copyfile(original, target)

    rs.MessageBox(message = "Publishing Done".format(res), buttons= 0 | 48, title = "EA monitor")









##########################################################################

if( __name__ == "__main__" ):

  publish_latest_toolbar()
