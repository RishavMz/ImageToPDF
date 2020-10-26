#author : RishavMz
# This program performs a simple task , to clear all the images from images file(probably after the conversion is over)
# to make the folder and the application ready for the next conversion 

import cv2
import inspect
import os

imagename = list()
path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
folder = path+'\images'
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename))
    if img is not None:
        print("Found ", filename)
        imagename.append(filename)
print('\n', len(imagename), 'images found')  
if(len(imagename) == 0):
    print("\n No image present in folder")
    quit(0)   
else:
    ch = input("Press F to clear all images from images folder and then Enter\n")  
    if(ch == 'F' or ch == 'f'):
        for data in range(len(imagename)):
            print("Removing", imagename[data])
            os.remove('images/'+(imagename[data]))         
        print('\n==========\n=  Done  =\n==========\n')            
        no = input("Press enter key to continue")  