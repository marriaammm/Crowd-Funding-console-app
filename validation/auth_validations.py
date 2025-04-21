import re
import getpass

EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
PHONE_REGEX = re.compile(r"^01[0125]\d{8}$")  

def valid_email(email):
    return EMAIL_REGEX.match(email) is not None

def valid_phone(phone):
    return PHONE_REGEX.match(phone) is not None

def get_valid_input(prompt, validate_fn, error_msg) :
    while True:
        value = input(prompt).strip()
        if validate_fn(value):
            return value
        print(error_msg)

def get_confirmed_password() :
    while True:
        pwd = getpass.getpass("Password: ").strip()
        confirm = getpass.getpass("Confirm password: ").strip()
        if pwd == confirm:
            return pwd
        print("Passwords do not match. Please try again.")
