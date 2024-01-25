import re

def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return False
    # Check for uppercase and lowercase letters
    if not (any(c.isupper() for c in password) and any(c.islower() for c in password)):
        return False
    # Check for at least one digit
    if not any(c.isdigit() for c in password):
        return False
    # Check for at least one special character
    if not re.search(r'[!@#$%]', password):
        return False
    # If all checks pass, return True
    return True

# Script to take user input and validate password
password = input("Enter your password: ")
if check_password_strength(password):
    print("Your password is strong.")
else:
    print("Your password does not meet the criteria.")