from docx2pdf import convert
import os, inspect, sys

filename = sys.argv[1] 

path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
inputpath = path+'\..\data\doc\\'+filename+'.docx'
filename = path+'\..\PDF\\'+filename+'.pdf'

convert(inputpath,filename)