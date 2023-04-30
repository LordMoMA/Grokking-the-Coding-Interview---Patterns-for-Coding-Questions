class CreateAccountError(Exception):
    pass


def create_account(username, password):
    if not username:
        raise CreateAccountError("Username is required")
    if not password:
        raise CreateAccountError("Password is required")
    # code to create account goes here


try:
    create_account("", "password123")
except CreateAccountError as e:
    print("An error occurred creating the account:", e)
