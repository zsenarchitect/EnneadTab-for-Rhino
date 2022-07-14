import shutil
import sys
import os
import time
import rhinoscriptsyntax as rs
import scriptcontext as sc
sys.path.append(r'L:\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\lib')
import EA_UTILITY as EA
import sys




def clear_text():
        all_text = rs.ObjectsByType(512)
        for text in all_text:
            try:
                if "monitoring sync queue" in rs.TextObjectText(text):
                    rs.DeleteObject(text)
            except:
                pass

def read_file_safely(original_path, local_path):
    shutil.copyfile(original_path, local_path)
    content = EA.read_txt_as_list(local_path)
    return content


def start_monitoring(revit_name = None, user_name = None):


    clear_text()

    if len( rs.AllObjects()) != 0:
        rs.MessageBox(message = "Prefer EMPTY Rhino file to begin with.", buttons= 48, title = "EnneadTab")
        return


    if user_name is None:
        user_name_to_check = rs.StringBox(message = "What is your Revit user name?", default_value = EA.get_sticky_longterm("SYNC_QUEUE_USER_NAME", "BIM360 account name or local username"), title = "EnneadTab")
    else:
        user_name_to_check = user_name
    EA.set_sticky_longterm("SYNC_QUEUE_USER_NAME", user_name_to_check)


    extension = ".queue"
    folder = r"L:\4b_Applied Computing\01_Revit\04_Tools\08_EA Extensions\Project Settings\Sync_Queue"


    if revit_name is None:
        revit_file = "2135_BiliBili SH HQ_N3"
        file_names = os.listdir(folder)
        options = [x.replace("Sync Queue_", "").replace(extension, "") for x in file_names]
        revit_file = EA.select_from_list(options,
                            title = "EnneadTab",
                            message = "Pick files to monitor sync queue",
                            muti_select = False,
                            button_names = ["Start Monitoring"],
                            width = 500,
                            height = 500)[0]
        if revit_file is None:
            return
    else:
        revit_file = revit_name


    file = "Sync Queue_" + revit_file
    original_path = folder + "\\" + file + extension
    local_folder = "{}\Documents\EnneadTab Settings\Sync_Queue_Monitor".format(os.environ["USERPROFILE"])
    try:
        os.makedirs(local_folder)
    except:
        pass
    local_path = "{}\{}{}".format(local_folder, file, extension)


    clear_text()




    note = rs.AddText("Currently monitoring sync queue for [{}].\nTime since monitoring begin = 0 seconds = 0 mins\n\nMonitor will terminate after until  iterations reached.\nWhen you are the first in the waiting list, the iteration will pause.\n\nYou can keep working on Revit.".format(revit_file), [0,0,0])
    rs.UnselectAllObjects()
    rs.SelectObject(note)
    try:
        if not rs.IsViewMaximized("Top"):
            rs.MaximizeRestoreView( "Top" )
    except Exception as e:
        print e
    rs.ZoomSelected()



    max_iteration = int(60 * 15) #this should give 15mins of monitoring session
    #max_iteration = int(30) # for testing, do 5 seconds
    for i in range(max_iteration + 1):
        time.sleep(1)
        rs.Redraw()
        text = "Currently monitoring sync queue for [{}].\nTime since monitoring begin = {} seconds = {} mins\n\nMonitor will terminate after until {} iterations reached.\nWhen you are the first in the waiting list, the iteration will pause.\n\nYou can keep working on Revit.".format(revit_file, i, i/60, max_iteration)
        #print text
        rs.TextObjectText(note, text = text)
        content = read_file_safely(original_path, local_path)
        if len(content) == 0:

            #consider exit rhino. When next time queue formed, fire another rhino
            continue
        if user_name_to_check not in content[0]:
            is_waiting = True
        else:
            EA.toast(message = "Revit file monitoring = [{}]".format(revit_file),
                    title = "You are at the front of sync queue")
            rs.MessageBox("It is your turn for syncing.")
            while True:
                content = read_file_safely(original_path, local_path)
                time.sleep(1)
                if len(content) == 0:
                    break
                if user_name_to_check in content[0]:
                    continue
                else:
                    break


if __name__ == "__main__":

    try:
        rs.Command("Fullscreen")
        start_monitoring()
        rs.MessageBox("Current sync queue monitor session finished.\n\nRun it again to monitor a new session.")
        rs.Command("Fullscreen")

    except KeyboardInterrupt:
        sys.exit()
