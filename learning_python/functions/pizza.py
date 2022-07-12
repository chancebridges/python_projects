def make_pizza(*toppings):
    """print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# the asterisk in the parameter name *toppings tells python to make an 
# empty tuple called toppings and pack whatever values it receives into this 
# tuple. 

# we can replace the print statement with a loop that runs through the list
# of toppings and describes the pizza being ordered.

# reference pizza_2.py