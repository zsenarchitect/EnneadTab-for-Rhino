import os
path = r"file:\\L:\4b_Applied Computing\01_Revit\04_Tools\08_EA Extensions\Library Docs\Codes\#PDF in this directory are reference only"


import subprocess
subprocess.Popen(r'explorer /select, {}'.format(path))
