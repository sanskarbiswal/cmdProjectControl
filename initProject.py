import sys, os
from github import Github

try:
    pDir = str(sys.argv[1])
    if os.path.exists("/"+pDir):
        print("\n*** Caution *** : Project Directory already Exists...")
        print("*** Please remove old directory before re-assigning ***\n")
        os.system("pause")
    else:
        os.mkdir(pDir) # Create Project Directory
        print("***Project Directory Created ***\n")
except IndexError:
    print("*** Error *** : No Project Name Assigned")



