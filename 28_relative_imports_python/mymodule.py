from libs import mylib

print("mymodule.py:", __name__)

# -- can't do relative imports from top-level file --

from .libs import mylib

# -- parent imports --

import libs.operations.operator
