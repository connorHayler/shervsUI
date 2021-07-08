import json
import hashlib
import uuid


# Function to hash passwords
def hash_password(pass_word):
    # Generate a random number to use as salt
    salt = uuid.uuid4().hex
    # Return hashed password
    return hashlib.sha256(salt.encode() + pass_word.encode()).hexdigest() + ':' + salt


# Function to check if password equals hashed password
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


# Function to register a new user
def register(user_name, pass_word, fname, lname):
    new_user = {'first_name': fname,
                'last_name': lname,
                'username': user_name,
                'password': pass_word,
                'type': "basic"}
    try:
        with open("credentials.json", "r+") as file:
            credentials_json = json.load(file)
            credentials_json["user"].append(new_user)
            file.seek(0)
            json.dump(credentials_json, file, indent=4)
            print("USER REGISTERED")
    except FileNotFoundError as err:
        return "File not found"


# Function to login
def login(user_name, pass_word):
    try:
        # Load exist user account from user account json file.
        with open("credentials.json", "r") as file:
            credentials_json = json.load(file)
            users_json = credentials_json["user"]

        # Check to see if username exists and what type of account it is
        for user in users_json:
            if user_name == user["username"]:
                # Check account type
                if user['type'] == "assistant":
                    if check_password(user['password'], pass_word):
                        print("PASSWORD ACCEPTED")
                        return "assistant"
                        break
                    else:
                        print("INCORRECT PASSWORD")
                        return False
                    break
                else:
                    if check_password(user['password'], pass_word):
                        print("PASSWORD ACCEPTED")
                        return "basic"
                        break
                    else:
                        print("INCORRECT PASSWORD")
                        return False
                    break
        else:
            print("No account with that username")
            return False

    except FileNotFoundError as err:
        return "File not found."