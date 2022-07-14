import rhinoscriptsyntax as rs
import scriptcontext as sc
import shutil

def copy_folder(source_folder, target_forlder, copy = True):

    pass


def publish_latest_toolbar():
    options = ["Exit without action", "Confirm"]
    res = rs.ListBox(items = options, message =  "Wait...Only proceed if your name is Sen Zhang", title = "STOP!", default = options[0])
    if res != options[1]:
        return

    save_res = rs.SaveToolbarCollection("EnneadTab")
    #rs.MessageBox(message = "saving 'EnneadTab.rui' file = {}".format(res), buttons= 0 | 48, title = "EA monitor")

    original = r"L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Working\EnneadTab.rui"
    target = r"L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\EnneadTab for Rhino\EnneadTab.rui"

    #copy rui file from working folder to L drive
    shutil.copyfile(original, target)

    """
    import os
    #copy L drive folders and files, including all source code, to my document folder github path.
    # source_dir = r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino'
    source_dir = r'P:\temp\source'
    destination_dir = r'P:\temp\tartget'
    # destination_dir = r'{}\Desktop\test'.format(os.environ["USERPROFILE"])
    shutil.copytree(source_dir, destination_dir)
    """

    import sys
    sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib')
    import EA_UTILITY as EA
    import EA_FORMS
    reload(EA)
    reload(EA_FORMS)

    #add alias for this
    EA.add_alias_set()

    toolbar_details = ""
    names = rs.ToolbarCollectionNames()
    if names:
        for name in names:
            toolbar_details += "\t\t\t\t{}:   {}\n".format(name, rs.ToolbarCollectionPath(name))

    rs.TextOut(message = "Current Toolbar Collection\n{}".format(toolbar_details))

    #rs.MessageBox(message = "Publishing Done.\n\nSave 'EnneadTab.rui' file = {}".format(save_res), buttons= 0 | 48, title = "EA monitor")
    EA.toast(message = r'Save "EnneadTab.rui" file = {}'.format(save_res), title = "Publishing Done.")








##########################################################################

if( __name__ == "__main__" ):

  publish_latest_toolbar()
