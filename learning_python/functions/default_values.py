# when writing a function, you can define a default value for each parameter
# if an argument for a parameter is provided in the function call, python uses the argument value.
# if there is no argument provided, it uses the parameter's default value.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')