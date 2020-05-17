# IMPORT MODULES
from sys import exit as e
# DECLARE CONSTANTS
VERSION = "N/A" #version of Todolist
# detect python version
try: 
    hi = raw_input #will raise a NameError if Python 3.x
    PYTHON_TWO = True #because if that completed successfully, it is python 2.x
except NameError:
    PYTHON_TWO = False
if PYTHON_TWO is True:
    e("Unsupported Python version: 2.x")
