def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(3, 5))
print(multiply(-1))

# The asterisk takes all the parameters and packs them into a tuple.
# The asterisk can be used to unpack sequences into arguments too!


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))  # instead of add(nums[0], nums[1])

# -- Uses with keyword arguments --
# Double asterisk packs or unpacks keyword arguments


def add(x, y):
    return x + y


nums = {"x": 15, "y": 25}

print(add(**nums))

# -- Unpacking kwargs --
def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)
# named({"name": "Bob", "age": 25})  # Error, the dictionary is actually a positional argument.
named(
    **{"name": "Bob", "age": 25}
)  # Unpack dict into arguments. This is OK, but slightly more confusing. Good when working with variables though.

# -- Unpacking and repacking --
def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)  # Unpack the dictionary into keyword arguments.
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)

# -- Forced named parameter --


def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        raise ValueError("No valid operator provided to apply().")


print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 5, "+"))  # Error

# -- Both --


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
