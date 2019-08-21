from libs.operations import operator

print("mylib.py:", __name__)

# -- can do relative imports from file with parent package --

from .operations import operator
