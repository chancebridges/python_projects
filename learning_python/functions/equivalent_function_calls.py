# because positional arguments, keyword arguments, and default values can all 
# be used together, often you'll have several equivalent ways to call a function

def describe_pet(pet_name, animal_type='dog'):

    # A dog named Willie.
    describe_pet('willie')
    describe_pet(pet_name='willie')

    # a hamster named Harry.
    describe_pet('harry', 'hamster')
    describe_pet(pet_name='harry', animal_type='hamster')
    describe_pet(animal_type='hamster', pet_name='harry')

# it doesn't matter what calling style you use, just use the style you find easiest