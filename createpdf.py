#author : RishavMz
# This file is for converting any docx file to pdf file.
# This file might be accessed when user chooses not to convert to pdf while making docx file , 
# and after reviewing docx file wishes to convert the docx file to pdf format

from docx2pdf import convert

filename = input("Enter filename ( excluding .docx extension) \n")
print("\n Please wait until the process is completed....\nThis may take a minute\nYou will be displayed a success message after completion\n")
convert(filename+".docx")
convert(filename+".docx",'PDF/',filename+".pdf")
convert("PDF/")
print("\nSuccessfully converted PDF file. \nPlease check the PDF folder\n\n")
no = input("Press enter key to continue")