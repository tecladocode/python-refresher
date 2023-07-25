x, y = 5, 11

# x, y = (5, 11)

# -- Destructuring in for loops --

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


# -- Another example --

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")


# -- Much better than this! --

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")


# -- Ignoring values with underscore --

person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)  # Bob Mechanic


# -- Collecting values --

head, *tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(tail)  # [2, 3, 4, 5]


*head, tail = [1, 2, 3, 4, 5]

print(head)  # [1, 2, 3, 4]
print(tail)  # 5

# -- Packing and unpacking --

# This isn't actually the end of the story, as there are also ways to pack and unpack collections using * and **, but that's a bit more advanced and you'll learn about it later on!
