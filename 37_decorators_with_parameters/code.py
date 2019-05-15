import functools

user = {"username": "anna", "access_level": "user"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return "admin: 1234"


@make_secure
def get_dashboard_password():
    return "user: user_password"


# What if we wanted some passwords to be available to "user" and others to "admin" ?

user = {"username": "anna", "access_level": "user"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."

        return secure_function

    return decorator


@make_secure(
    "admin"
)  # This runs the make_secure function, which returns decorator. Essentially the same to doing `@decorator`, which is what we had before.
def get_admin_password():
    return "admin: 1234"


@make_secure("user")
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())

user = {"username": "anna", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())
