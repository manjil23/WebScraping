import os

#reading the file's in the folder
folderpath = r"C:\Users\mlpradhan\OneDrive - alliedelec.com\Desktop"
os.chdir(folderpath)

#check for files in the folderpath
print(os.listdir())