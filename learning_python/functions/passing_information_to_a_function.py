# to pass information to a function, you enter a value name in the parentheses
# of the function. by adding this you allow the function to accept a value that
# you specify. 

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')