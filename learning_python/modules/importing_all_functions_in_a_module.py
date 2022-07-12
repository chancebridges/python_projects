# you can tell python to import every function in a module by using
# the asterisk (*) operator:

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# the asterisk in the import statement tells python to copy every function 
# from the module pizza into this program file. because every funciton is
# imported, you can call each function by name without using the dot notation. 

# the best approach is to import the function or functions you want, or import
# the entire module and use the dot notation

# from module_name import *