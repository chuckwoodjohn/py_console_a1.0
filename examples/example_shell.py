# Import the console package
from console_a10 import *
# Import the dcl modules
import example
# Define the current module
from sys import modules; THIS=modules[__name__]
# Initialize the shell
test_shell = shell.Shell(module=THIS, dcls=["example.dcl"])
# Run the shell
test_shell.mainloop()
