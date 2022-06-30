# when you pass a list to a funciton, the function gets direct
# access to the contents of the list

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# We define greet_users() so it expects a list of names, which it stores in 
# the parameter names. 

# the function loops through the list it receives and prints a greeting to each user