import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms, ')

# when python reads this file, the line import pizza tells python to open the
# file pizza.py and copy all the functions from it into this program.

# all you need to know is that any function defined in pizza.py will now
# be available in making_pizzas.py

# to call a function from an imported module, enter the name of the module
# you imported, pizza, followed by the name of the function, make_pizza()
# , separated by a dot. 

