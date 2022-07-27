import shutil
import os
source=input("enter the shource folder name")
destination=input("enter the destination folder name")
source=source+'/'
destination=destination+'/'

listOfFiles=os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),destination)