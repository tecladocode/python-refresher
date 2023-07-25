def add(x, y=3):
    print(x + y)


add(5)  # 8
add(5, 8)  # 13
add(y=3)  # Error, missing x

# -- Order of default parameters --

# def add(x=5, y):  # Not OK, default parameters must go after non-default
#     print(x + y)

# -- Usually don't use variables as default value --

default_y = 3


def add(x, y=default_y):
    sum = x + y
    print(sum)


add(2)  # 5

default_y = 4
print(default_y)  # 4

add(2)  # 5, even though we re-defined default_y
