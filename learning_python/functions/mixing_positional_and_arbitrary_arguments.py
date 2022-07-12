# if you want a function to accept several different kinds of arguments, the 
# parameter that accepts an arbitrary number of arguments must be placed last
# in the function definition.

# python matches positional and keyword arguments first and then collects any
# remaining arguments in the final parameter. 

# for example look below at how the positional and arbitrary arguemtn are listed

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
         "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# In the function definition, python stores the first value it receives in 
# the parameter size. All other values that come after are stored in the tuple
# "toppings". The function calls include an argument for the size first, 
# followed by as many toppings as needed. 