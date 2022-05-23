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

    #also reload python engine for EA module
    import sys
    sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib')
    import EA_UTILITY as EA
    import EA_FORMS
    reload(EA)
    reload(EA_FORMS)


    #add alias for this
    EA.add_alias_set()

    rs.MessageBox(message = "Latest EnneadTab Loaded.\n\nPreviously docked EnneadTab can be removed from your UI.", buttons= 0 | 48, title = "EA monitor")






##########################################################################

if( __name__ == "__main__" ):

  get_latest_toolbar()
