users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}
userid_mapping = {user[0]: user for user in users}

print(username_mapping)

print(username_mapping["Bob"])  # (0, "Bob", "password")

# -- Can be useful to log in for example --

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect.")

# If we didn't use the mapping, the code would require us to loop over all users.
# Shown on the side, pause the video if you want to read it thoroughly.
