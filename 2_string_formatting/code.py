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
