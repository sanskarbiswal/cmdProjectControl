import os, sys
from github import Github

uName = "sanskarbiswal"
pwd = "Dante1234@"
pDir = sys.argv[1]
# Open Github and Create Repository
user = Github(uName, pwd).get_user()
repo = user.create_repo(pDir)
print("\n*** Git Repo Created with name : {}", format(pDir))
print("\n")

# git command set
os.system("git init")
os.system("type nul > README.me")
os.system("git add .")
os.system("git commit -m 'Init'")
os.system("git remote add origin https://github.com/sanskarbiswal/"+pDir+".git")
os.system("git push -u origin master")
print("\n*** Project Structure Created ***\n")
os.system("pause")
os.system("code .")