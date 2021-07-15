from docx2pdf import convert
import os, inspect, time

filename = str(round(time.time()*1000000))+".pdf"

path= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
path = path+'\..\data\doc\sample.docx'

convert(path,'PDF/',filename)