# cmdProjectControl

Very often when working on projects, I find it to be a little inconvinient to always follow the process of going through the creating a folder, create files, then a new repository etc. Thus, when I came across a video on youtube to automate the process, I began to work on this.
In its current form, the project allows me to preset a fixed location in my system in a *.bat* file which I use as my default project directory. So, everytime I want to create a new project, in my command prompt, I input the following command:
  > initProject *projectName*
This command, creates a folder, then opens a new github repo and finally opens Visual Studio Code in that project directory.

## Method to install requsite python modules
python3 -m pip install Github 

## Commands Included
  > initProject
  
  > rmvProject
  
  > ls

## Method to access commands from cmd

1. Save the files of the repo, in the Projects folder
2. Goto *Advanced Environment Settings* and add the path of the project folder to the PATH
3. Restart computer

# Note
  > The codes given here are tested on Windows 10 platform only. 
  
  > The default project folder here is F-drive. To make changes, the drive location needs to be changes in all files. 
