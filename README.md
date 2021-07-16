<center>

<b>A GUI based Image to PDF converter which allows user to select a list of images from his PC and add them to a single PDF file.</b>

<code><img src="https://raw.githubusercontent.com/RishavMz/ImageToPDF/master/data/ImageToPDF.png" height="500"></code>
</center>


## How to run this application on your machine

### System requirements( must be already present/installed )
1. Windows OS
2. Microsoft Office
3. Python3
4. C++ compiler

### Install dependencies
```
pip install -r requirements.txt 
```

### Compile GUI.cpp file
```
g++ gui.cpp -lcomdlg32
```

### Run the executable file generated

#

### File Structure:

* data
    - database
        + imageselected.txt  ====>  `Temporarily stores the list of images to be added to the PDF file`
    - doc
        +  ====>  `Stores the intermediate .docx file which is to be later converted into PDF format`
* PDF   
    -  ====>  `Stores the converted PDF files`
* scripts
    -  ====>  `Contains the python scripts which perform the required operation`
* gui.cpp  ====>  `Handles the core interface of the application including GUI`
* requirements.txt  ====>  `Contains list of dependancies for the python scripts to run properly`