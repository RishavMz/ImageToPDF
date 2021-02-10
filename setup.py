from cx_Freeze import setup, Executable

base = None    

executables = [Executable("gui.py", base=base)]

packages = ["idna", "os","sys"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Image_To_PDF",
    options = options,
    version = "2.0",
    description = 'A GUI based desktop application developed using python',
    executables = executables
)