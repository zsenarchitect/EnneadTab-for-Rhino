print "this is EA startup file"
import rhinoscriptsyntax as rs
import EA_UTILITY as EA


def monitor_revit_sync():

    import sys
    sys.path.append(r'L:\\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\Revit')
    import sync_queue_monitor

    """
    import imp
    ref_module = imp.load_source("sync_queue_monitor", r'L:\\4b_Applied Computing\03_Rhino\12_EnneadTab for Rhino\Source Codes\Revit\sync_queue_monitor.py')
    """
    doc_name = rs.DocumentName()
    if doc_name is None:
        return
    if "EA_SYNC_QUEUE" not in doc_name:
        return


    revit_name = doc_name.split("#")[1]
    user_name = doc_name.split("#")[2] #.split(".3dm")[0]
    #print "Doing something in {}".format(doc_name)
    EA.toast(title = "Start Revit Sync Monitor", message = "Revit file monitoring = [{}]".format(revit_name))

    rs.Command("Fullscreen")
    sync_queue_monitor.start_monitoring(revit_name, user_name)
    rs.DocumentModified(False)
    #rs.Command("_-New _None", False)
    rs.Exit()




##################### main code below #################
if __name__ == "__main__":
    monitor_revit_sync()
