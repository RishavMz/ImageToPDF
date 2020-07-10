#Author : RishavMz
#
#   This file combines the function from all the other files to generate an interactive GUI based application for the
#   program using tkinker. This is just a GUI variation of the entire application with some minor changes. 
#   
#   Hope you like it :)

import tkinter
from tkinter import *

def convert1():
    print("Converted to docx / PDF format ")
def convertfn():
    convert = tkinter.Tk() 
    convert.title("Images to PDF / docx format")
    w = Canvas(convert, width=40, height=60) 
    w.pack() 
    canvas_height=20
    canvas_width=200
    label1 = Label(convert,text = "Please make sure that you have added all photos to be inserted in pdf serially in the images folder\n\n")
    label1.pack()
    name = Label(convert,text = "Please enter a name for your docx / PDF file\n")
    name.pack()
    nameentry = Entry(convert)
    nameentry.pack()
    space = Label(convert,text = "\n")
    space.pack()
    button1 = tkinter.Button(convert, text='Convert to PDF/docx', width=35, command = convert1)
    button1.pack()
    space = Label(convert,text = "\n")
    space.pack()
    convert.mainloop()

def createpdf1():
    print("Converted from docx to pdf format")
def createpdffn():
    createpdf = tkinter.Tk() 
    createpdf.title("docx to pdf format")
    w = Canvas(createpdf, width=40, height=60) 
    w.pack() 
    canvas_height=20
    canvas_width=200
    label1 = Label(createpdf, text = "Please enter the filename of the docx file ( without docx entension to convert it into PDF format)\n\n")
    label1.pack()
    fnameentry = Entry(createpdf)
    fnameentry.pack()
    space = Label(createpdf,text = "\n")
    space.pack()
    button1 = tkinter.Button(createpdf, text='Convert to PDF/docx', width=35, command = createpdf1)
    button1.pack()
    space = Label(createpdf,text = "\n")
    space.pack()
    createpdf.mainloop()

def clearimagesfn():
    print("Deleted all images from IMAGES folder")

master = tkinter.Tk() 
master.title("Images to PDF converter")
w = Canvas(master, width=40, height=60) 
w.pack() 
canvas_height=20
canvas_width=200

l1 = Label(master,text="This is a simple program to convert Images into docx / PDF file format.\n\nPlease add all the images you want to add to your PDF in the images folder.\nIf you have not, conversion might cause an error.\n\n")
l1.pack()

button1 = tkinter.Button(master, text='Convert Images to PDF/docx', width=35, command = convertfn)
button1.pack()
space = Label(text = "\n")
space.pack()

button1 = tkinter.Button(master, text='Convert docx file to PDF', width=35, command = createpdffn)
button1.pack()
space = Label(text = "\n")
space.pack()

button1 = tkinter.Button(master, text='Clear images from the Images folder', width=35, command = clearimagesfn)
button1.pack()
space = Label(text = "\n")
space.pack()
master.mainloop()