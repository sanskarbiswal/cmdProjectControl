import sys, os
from github import Github

pDir = str(sys.argv[1])

ch = input("Proceed with scrapping Project Folder " +pDir+" (y/n) : ")

if (ch=="Y" or ch=="y"):
    if pDir in os.listdir("F:/"): # Since F-Drive is the Project Directory
        print("Project Directory Found... Starting Clean Up...")
        user = Github("sanskarbiswal", "Dante1234@").get_user()
        repo = user.get_repo(pDir)
        repo.delete()
        os.system("rmdir /s "+pDir)
        print("\nProject Tree Removed Successfully\n")
        os.system("pause")
    else:
        print("*** ERROR *** : This Project Directory is not on the System")
        print("\n\n*** PLEASE VERIFY ***\n")
        os.system("pause")
elif (ch=="N" or ch=="n"):
    print("*** Terminating Operation ***\n")
    os.system("pause")
else:
    print("*** Invalid Option ***\n")
    os.system("pause")