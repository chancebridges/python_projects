import json

#username = input("What is your name? ")

#filename = 'username.json'
#with open(filename, 'w') as f_obj:
#    json.dump(username, f_obj)
#   print("We'll remember you when you come back, " + username + "!")

# At line 3 we prompt for a username to store.

# At line 7 we use json.dump(), passing it a username and a file object
#, to store the username in a file. 

# At line 8 we print a message informing the user that we've stored their information. 

# now lets write a program that greets a user whose name has already been stored:
# reference greet_user.py


# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it. 
#filename = 'username.json'
#try:
#    with open(filename) as f_obj:
#        username = json.load(f_obj)
#except FileNotFoundError:
#    username = input("What is your name? ")
#    with open(filename, 'w') as f_obj:
#        json.dump(username, f_obj)
#        print("We'll remember you when you come back, " + username + "!")
#else:
#    print("Welcome back, " + username + "!")
    
    # At line 25 we try to open the file username.json
    
    # at line 26, if the file exists, we read the username back into memory and 
    # prints a message welcoming back the user in the else block. 
    
    # If this is the first time the user runs the program, username.json will not
    # exist and a FileNotFoundError will occur (line 27)
    
#def greet_user():
#    """Greet the user by name."""
#    filename = 'username.json'
#    try:
#        with open(filename)as f_obj:
#            username = json.load(f_obj)
#    except FileNotFoundError:
#        username = input("What is your name? ")
#        with open(filename, 'w') as f_obj:
#            json.dump(username, f_obj)
#            print("We'll remember you when you come back, " + username + "!")
#    else:
#        print("Welcome back, " + username + "!")
#
#greet_user()

# Lets refactor the above function

# lets start by moving the code for retreiving a stored username to a separate function

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
    
greet_user()

# The new function get_stored_username() has a clear purpose, as stated
# in the docstring. 