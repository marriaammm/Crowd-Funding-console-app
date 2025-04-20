from dependancies import load, save, USER_FILE, SESSION_FILE
from authValidations import valid_email, valid_phone, get_valid_input, get_confirmed_password
import getpass

def register():
    users = load(USER_FILE, default=[])

    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()

    email = get_valid_input("Email: ", valid_email, "Invalid email format. Please try again.")
    password = get_confirmed_password()

    phone = get_valid_input("Phone: ", valid_phone, "Invalid phone number format. Please try again.")

    users.append({
        "first": first_name,
        "last": last_name,
        "email": email,
        "password": password,
        "phone": phone
    })

    save(USER_FILE, users)
    save(SESSION_FILE, {"email": email})  
    print("Registration successful. You are now logged in.")

def login():
    email = input("Email: ").strip()
    password = getpass.getpass("Password: ").strip()
    users = load(USER_FILE, default=[])

    for user in users:
        if user["email"] == email and user["password"] == password:
            print("Login successful.")
            save(SESSION_FILE, {"email": email})
            return user

    print("Invalid email or password.")

def logout():
    session = load(SESSION_FILE, default={})
    if "email" in session:
        del session["email"]
        save(SESSION_FILE, session)
        print("Logged out successfully.")
    else:
        print("No user is logged in.")

def get_current_user():
    session = load(SESSION_FILE, default={})
    email = session.get("email")
    if not email:
        return None
    users = load(USER_FILE)
    return next((u for u in users if u["email"] == email), None)
