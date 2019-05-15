day_of_week = input("What day of the week is it today? ")

if day_of_week == "Monday":
    print("Have a great start to your week!")
elif day_of_week == "Friday":
    print("It's ok to finish a bit early!")
else:
    print("Full speed ahead!")

# -- Problem: user not entering what we expect --

day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "friday":
    print("It's ok to finish a bit early!")
else:
    print("Full speed ahead!")
