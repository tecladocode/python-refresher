def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(3, 5))
print(multiply(-1))

# The asterisk takes all the arguments and packs them into a tuple.
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
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 5, "+"))  # Error
