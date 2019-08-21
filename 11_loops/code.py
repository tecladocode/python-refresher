# -- While loop --

number = 7
play = input("Would you like to play? (Y/n) ")

while play != "n":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")

    play = input("Would you like to play? (Y/n) ")


# -- The break keyword --

while True:
    play = input("Would you like to play? (Y/n) ")

    if play == "n":
        break  # Exit the loop

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")


# -- For loop --

friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in friends:
    print(f"{friend} is my friend.")

# -- For loop 2 -- Average

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)

# -- Rewritten using sum() --

grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)

# You kinda just have to "know" that exists. It takes time and experience, but searching for almost _everything_ really helps. For example, you could've searched for "sum list of numbers python".
