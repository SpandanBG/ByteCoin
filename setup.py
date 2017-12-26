import sys
from cx_Freeze import setup, Executable
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

#os.environ['TCL_LIBRARY'] = 'C:/Users/HackRider/AppData/Local/Programs/Python/Python35/tcl/tcl8.6'
#os.environ['TK_LIBRARY'] = 'C:/Users/HackRider/AppData/Local/Programs/Python/Python35/tcl/tk8.6'

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

build_exe_option = {
    "packages": ["tkinter", "threading", "json", "requests", "time", "idna", "bin"],
    #"include_files": ['C:/Users/HackRider/AppData/Local/Programs/Python/Python35/DLLs/tcl86t.dll', 'C:/Users/HackRider/AppData/Local/Programs/Python/Python35/DLLs/tk86t.dll', "config\cryptocurrencies.json", "config\icon.ico"]
    "include_files": [PYTHON_INSTALL_DIR+'\\DLLs\\tcl86t.dll', PYTHON_INSTALL_DIR+'\\DLLs\\tk86t.dll', ("config\cryptocurrencies.json", "config\cryptocurrencies.json"), ("config\icon.ico", "config\icon.ico")]
}

executable = [
    Executable('ByteCoin.py',
               base=base,
               icon='config/icon.ico'
               )
]

setup(
    name='ByteCoin',
    version='0.0.1',
    description='Bitcoin Purchase Price Calc',
	options={'build_exe': build_exe_option},
    executables=executable
)
