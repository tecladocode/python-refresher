def divide(dividend, divisor):
    return dividend / divisor


print("mymodule.py:", __name__)

# -- importing from a folder --

import libs.mylib

print("mymodule.py:", __name__)
