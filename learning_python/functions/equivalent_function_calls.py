# because positional arguments, keyword arguments, and default values can all 
# be used together, often you'll have several equivalent ways to call a function

def describe_pet(pet_name, animal_type='dog')

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

