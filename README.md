# Image-To-PDF-using-Python
A python based desktop application to automate the extremely slow and boring task of copying and pasting images to docx file and further resizing 
    
    .
    
This application automises the boring procedure of copying all images and pasting in document which is very slow process,
and may also sometimes lead to freezing of your application. However, this is extremely fast compared to 
performing the same task in word processing softwares. Moreover, this program resizes the images taking into account the aspect ratio
of the images which further minimizes the boring task of formatting each image one by one.    


    ===========================================================================================
    ===                             INSTRUCTIONS                                            ===
    ===========================================================================================

    Follow the steps:(installation)

    1. Download python from
    2. Run the exe file to get python installed in your system.
    3. Open the folder containing this application.
    4. Run the setup.py program to get the dependencies for this application downloaded in your system.
    5. Now, you are ready. Installation is complete.


    *********************************************************************************************

    Note - This application performs two steps.
        First it collects the images and converts them to a docx format, 
        and then in the second step, it converts the docx file into a PDF file. 

    Steps to convert images to pdf:

    1. Copy all the images you want to be present in the pdf file and paste them in IMAGES folder of this application.
    2. Order the images by their names. The images would be in the docx and then in pdf file based on the sorted order by names.
    3. Run the convert.py file To collect images from images from IMAGES folder and convert it to docx file. Then the application promts the user .
    4. If you want to have a look at the docx file before conversion to pdf format, then press any key other than 1 and press enter. Search the file by name given earlier and view it in any text editor. Later, you can Run the createpdf.py file to convert the docx file to pdf format.
    5. If you want to directly convert to pdf from images, press 1 and then press enter.
    6. The conversion to pdf may take some time. Please wait until the program shows a success message.
    7. You can find the pdf in the PDF file.
    8. After completion, you can run the clearimages.py file to clear the IMAGES folder for further next new conversions.

    ==================================================================================================

    ##################################################################################################

        ++++++++++++++++++++++++++++++++++++++
        +   Hope you like this application.  +
        +                                    +
        +    Author                          +
        +      RishavMz                      +
        ++++++++++++++++++++++++++++++++++++++



Python libraries used:

    1. Python-docx
    2. Python-opencv
    3. Python docx2pdf
