class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


bob = Person("Bob", 35)
print(bob)  # Not the nicest thing to read!

# -- __str__ --
# The goal of __str__ is to return a nice, easy to read string for end users.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old"


bob = Person("Bob", 35)
print(bob)  # Much nicer

# -- __repr__ --
# The goal of __repr__ is to be unambiguous, and if possible what it outputs should allow us to re-create an identical object.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        # I'm adding the < > just so it's clear that this is an object we're printing out!
        return (
            f"<Person({self.name!r}, {self.age})>"
        )  # !r calls the __repr__ method of the thing.


bob = Person("Bob", 35)
print(bob)  # Not as nice, but we could re-create "Bob" very easily.
