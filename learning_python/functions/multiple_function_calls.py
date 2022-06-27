# you can call a function as many times as needed
# describing a second, different pet requires just one more call to describe_pet()

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is "+  pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
