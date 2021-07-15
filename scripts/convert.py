from docx2pdf import convert
import os, inspect, sys

filename = sys.argv[1] 

filename = filename+".pdf"

path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
path = path+'\..\data\doc\sample.docx'

convert(path,'PDF/',filename)