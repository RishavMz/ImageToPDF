#author : RishavMz
# This is a setup file, which must be run before any other program file.
# This file installs all the required python libraries for this application.

import subprocess

subprocess.run('pip install python-docx')
subprocess.run('pip install opencv-python')
subprocess.run('pip install docx2pdf')