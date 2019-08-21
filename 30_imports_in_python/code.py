# -- importing --

from mymodule import divide

print(divide(10, 2))

# -- __name__ --

print(__name__)

# -- importing with names --

import mymodule

print("code.py: ", __name__)

# How does Python know where `mymodule` is?
# Answer, it looks at the paths in sys.path in order:

import sys

print(sys.path)

# The first path is the folder containing the file that you ran.
# The second path is the environment variable PYTHONPATH, if it is set.
# We won't cover environment variables in depth here, but they are variables you can set in your operating system. It can help Python find things to import when the folder structure is ambiguous.

# -- circular imports --
# Make mymodule.py import code.py as well.

# -- importing from a folder --

import mymodule

print("code.py: ", __name__)

import sys

print(sys.modules)
