name = "Bob"
greeting = "Hello, Bob"

print(greeting)

name = "Rolf"

print(greeting)

greeting = f"Hello, {name}"
print(greeting)

# --

name = "Anne"
print(
    greeting
)  # This still prints "Hello, Rolf" because `greeting` was calculated earlier.
print(
    f"Hello, {name}"
)  # This is correct, since it uses `name` at the current point in time.

# -- Using .format() --

# We can define template strings and then replace parts of it with another value, instead of doing it directly in the string.

greeting = "Hello, {}"
with_name = greeting.format("Rolf")
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)
