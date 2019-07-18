import sys, os
from github import Github

pDir = str(sys.argv[1])

ch = input("Proceed with scrapping Project Folder " +pDir+" (y/n) : ")

if (ch=="Y" or ch=="y"):
    if pDir in os.listdir("F:/"): # Since F-Drive is the Project Directory. Change if alternate drive is being used by you
        print("Project Directory Found... Starting Clean Up...")
        user = Github("username", "password").get_user() # add usn and pwd of your account to use
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
