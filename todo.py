# IMPORT MODULES
from sys import exit as e
import six
# DECLARE CONSTANTS
VERSION = "N/A" #version of Todolist
# detect python version
if six.PY2: #source https://stackoverflow.com/a/43481041/9654083
    e("Unsupported Python Version")
else:
    print("Welcome to Todolist!")
