# -- Unpacking kwargs --
def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)
# named({"name": "Bob", "age": 25})  # Error, the dictionary is actually a positional argument.

# Unpack dict into arguments. This is OK, but slightly more confusing. Good when working with variables though.
named(**{"name": "Bob", "age": 25})


# -- Unpacking and repacking --
def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)  # Unpack the dictionary into keyword arguments.
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


# -- Both args and kwargs --


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)

# This is normally used to accept an unlimited number of arguments and keyword arguments, such that some of them can be passed onto other functions.
# You'll frequently see things like these in Python code:

"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""

# While the implementation is irrelevant at this stage, what it allows is for the caller of `post()` to pass arguments to `request()`.

# -- Error when unpacking --


def myfunction(**kwargs):
    print(kwargs)


myfunction(**"Bob")  # Error, must be mapping
myfunction(**None)  # Error
