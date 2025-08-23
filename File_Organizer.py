#This Program organizes files according to their extensions.


import os
import shutil 

path = input("Enter the path of the folder you want to organize: ")
files = os.listdir(path)

for file in files:
    filename, extentions = os.path.splitext(file)
    extentions = extentions[1:]
    
    if os.path.exists(path+"/"+extentions):
        shutil.move(path+"/"+file, path+"/"+extentions+"/"+file)
    else:
        os.makedirs(path+"/"+extentions)

        shutil.move(path+"/"+file, path+"/"+extentions+"/"+file)
