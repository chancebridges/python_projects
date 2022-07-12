# you can call a function as many times as needed
# describing a second, different pet requires just one more call to describe_pet()

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is "+  pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# in the second function call, we pass describe_pet() the arguments 'dog' and 'willie'
# calling a function multiple times is a very efficient way to work
# you can use as many positional arguments as you need in your functions