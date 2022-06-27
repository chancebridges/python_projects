# when you call a function, python must match each argument in the function call with a parameter in the function definition.
# the simplest way to do this is based on the order of the argments provided.
# this is called positional arguments.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')