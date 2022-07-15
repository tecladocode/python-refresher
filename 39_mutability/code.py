a = []
b = a

# Remember a and b are _names_ for the list. They both have the _same_ value.

a.append(35)  # Modify the value.

print(a)
print(b)

# We mutated (changed) the value, its names still point to the _same thing_, so it doesn't matter which name you use.

a = []
b = []

a.append(35)

print(a)
print(b)

# Here they are different lists, because [] creates a new list every time. You can check whether two things are the _same_ one by usingt the `id()` function:

print(id(a))
print(id(b))  # Different from id(a)

# -- immutable --

# Some values can't be changed because they don't have methods that modify the value itself.
# In case of the list, `.append()` mutates the list.
# For example integers don't have any such methods, so they are called _immutable_.

a = 8597
b = 8597

print(id(a))
print(id(b))  # Same one

a = 8598

print(id(a))
print(
    id(b)
)  # Different, because we didn't change 8597. We just used the name 'a' for a different value. 'b' still is a name for 8597.

# Most things are mutable in Python. If you want to keep one of your classes immutable, don't add any methods that change the objects' properties.

# Tuples and strings are the only fundamental collection in Python which is immutable.
# Lists, sets, dictionaries are all mutable.
# Integers, floats, and booleans are all immutable.

# -- += and similar --

# A lot of beginners think this:

a = "hello"
b = a

print(id(a))
print(id(b))

a += "world"

# Would cause 'b' to change
# But it doesn't, because strings are immutable. When you do str + str, a _new_ string is created.
# This means that a becomes a new string containing "helloworld", but b still is a name for "hello".

print(id(a))
print(id(b))
