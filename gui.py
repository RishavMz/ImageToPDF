#Author : RishavMz
#
#   This file combines the function from all the other files to generate an interactive GUI based application for the
#   program using tkinker. This is just a GUI variation of the entire application with some minor changes. 
#   
#   Hope you like it :)

import tkinter
from tkinter import *
from docx2pdf import convert
from docx import Document
from docx.shared import Inches, Cm
import cv2
import os
import inspect
from docx2pdf import convert
from tkinter.filedialog import askopenfilename

images_name = list()
def convert1():
    converted = tkinter.Tk() 
    converted.title("Images to docx format completed")
    w1 = Canvas(converted, width=40, height=60) 
    w1.pack() 
    canvas_height=20
    canvas_width=200
    w1.create_text(0, 30, anchor=W, font="Purisa",
            text="PDF", fill="maroon")
    print("Converted to docx  format ")
    document = Document()
    size = list()
    imagename = list()
    for filename in images_name:
        img = cv2.imread(os.path.join('',filename))
        if img is not None:
            print("Found ", filename)
            imagename.append(filename)
            image = img.shape
            width = img.shape[0]
            height = img.shape[1]
            size.append([width,height])
    print('\n', len(imagename), 'images found')  
    if(len(imagename) == 0):
        print("\n No image present in folder")
        label1 = Label(converted,text = "No images found in Images folder!!! \nCreated a blank docx file\n")
        label1.pack()
    name = "sample"
    name = name+'.docx'
    print(name)
    for data in range(len(imagename)):
        print("Processing ",imagename[data])
        p = document.add_paragraph()
        r = p.add_run()
        #print(size[data])
        if (size[data][0] / size[data][1] >=1.5):
            #print("Type1")
            r.add_picture(str(imagename[data]), height = Cm(27) , width = Cm(27/size[data][0]*size[data][1]))    
        elif (size[data][0] / size[data][1] >=1 ):
            #print("Type2")
            r.add_picture(str(imagename[data]), height = Cm(24) , width = Cm(24/size[data][0]*size[data][1]))    
        else:
            #print("Type3")
            r.add_picture(str(imagename[data]), width = Cm(21.4) , height = Cm(21.4/size[data][1]*size[data][0]))

    widmargin = 0.1
    lenmargin = 0.5    
    sections = document.sections
        
        # Page margins narrowed
    for section in sections:
        section.top_margin = Cm(lenmargin)
        section.bottom_margin = Cm(lenmargin)
        section.left_margin = Cm(widmargin)
        section.right_margin = Cm(widmargin)  
    document.save(name)
    print('\n==========\n=  Done  =\n==========\n')
    print("Successfully created a docx file\n")
    label1 = Label(converted,text = "Successfully created a docx file\n")
    if(len(imagename)>0):
        label1.pack()
    converted.mainloop()


def convertfn():
    convert = tkinter.Tk() 
    convert.title("Images to docx format")
    w2 = Canvas(convert, width=40, height=60) 
    w2.pack() 
    canvas_height=20
    canvas_width=200
    w2.create_text(0, 30, anchor=W, font="Purisa",
            text="PDF", fill="maroon")
    label1 = Label(convert,text = "Please make sure that you have added all photos to be inserted in pdf serially in the images folder\n\n")
    label1.pack()
    name = Label(convert,text = "Please note, the name of docx/PDF file would be sample.docx/sample.pdf by default.\n You can rename it later\n")
    name.pack()
    space = Label(convert,text = "\n")
    space.pack()
    button1 = tkinter.Button(convert, text='Convert to docx', width=35, command = convert1)
    button1.pack()
    space = Label(convert,text = "\n")
    space.pack()
    convert.mainloop()

def createpdf1():
    print("Converted from docx to pdf format")
    convertedpdf = tkinter.Tk() 
    convertedpdf.title("Images to docx format completed")
    w1 = Canvas(convertedpdf, width=40, height=60) 
    w1.pack() 
    canvas_height=20
    canvas_width=200
    w1.create_text(0, 30, anchor=W, font="Purisa",
            text="PDF", fill="maroon")
    print("\n Please wait until the process is completed....\nThis may take a minute\nYou will be displayed a success message after completion\n")
    convert("sample.docx",'PDF/',"sample.pdf")
    lab2 = Label(convertedpdf , text = "Successfully converted PDF file. \nPlease check the PDF folder to find the converted PDF file\n\n")
    lab2.pack()
    print("\nSuccessfully converted PDF file. \nPlease check the PDF folder to find the converted PDF file\n\n")

def createpdffn():
    createpdf = tkinter.Tk() 
    createpdf.title("docx to pdf format")
    w3 = Canvas(createpdf, width=40, height=60) 
    w3.pack() 
    canvas_height=20
    canvas_width=200
    w3.create_text(0, 30, anchor=W, font="Purisa",
            text="PDF", fill="maroon")
    label1 = Label(createpdf, text = "Please note. The latest sample.docx file created within the project folder would be \n converted to PDF format under the name sample.pdf\n Please make sure you perform this operation after conversion \n of images into docx file format.\n")
    label1.pack()
    space = Label(createpdf,text = "\n")
    space.pack()
    button1 = tkinter.Button(createpdf, text='Convert to PDF', width=35, command = createpdf1)
    button1.pack()
    space = Label(createpdf,text = "\n")
    space.pack()
    lab1 = Label(createpdf , text = " Please wait until the process is completed....\nThis may take a minute\nYou will be displayed a success message after completion\n\nNo need to click the above button more than once.\n Sorry, but this process is a bit slow.\n\n")        
    lab1.pack()
    createpdf.mainloop()

def addimagesfn():
    adding = tkinter.Tk() 
    adding.title("Add images")
    w4 = Canvas(adding, width=40, height=60) 
    w4.pack() 
    canvas_height=20
    canvas_width=200
    w4.create_text(0, 30, anchor=W, font="Purisa",
            text="PDF", fill="maroon")
    print("Selecting images to add")
    while(True):
        path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        images_name.append(path)
        if(len(path)<=0):
            break
    if(len(images_name) == 0):
        print("\n No image present in folder")
        label1 = Label(adding,text = "No image found in Images folder\n")
    else:
        for data in range(len(images_name)):
            print("Addng", images_name[data])
        print('\n==========\n=  Done  =\n==========\n')
        label1 = Label(adding,text = "Successfully added all images to memory\n")
    label1.pack()
    adding.mainloop()    
master = tkinter.Tk() 
master.title("Images to PDF converter")
w = Canvas(master, width=40, height=60) 
w.pack() 
canvas_height=50
canvas_width=200
w.create_text(0, 30, anchor=W, font="Prussia",
            text="PDF", fill="maroon")
l1 = Label(master,text="This is a simple program to convert Images into docx and then into PDF file format.\n\nPlease add all the images you want to add to your PDF in the images folder.\nIf you have not, conversion might cause an error.\n\n")
l1.pack()

button1 = tkinter.Button(master, text='Add images to convert into PDF', width=35, command = addimagesfn)
button1.pack()
space = Label(text = "\n")
space.pack()

button1 = tkinter.Button(master, text='Convert Images to docx', width=35, command = convertfn)
button1.pack()
space = Label(text = "\n")
space.pack()

button1 = tkinter.Button(master, text='Convert docx file to PDF', width=35, command = createpdffn)
button1.pack()
space = Label(text = "\n")
space.pack()

master.mainloop()
