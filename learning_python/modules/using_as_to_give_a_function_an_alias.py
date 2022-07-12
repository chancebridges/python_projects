# if the name of a function you're importing might conflickt with an existing
# name in your program, or if the function name is long, you can use a short
# unique alias. 

# below we give the funcitonmake_pizza() an alias, mp(), by importing
# make_pizza as mp. the keyword renames a function using the alias you provide:

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# the import statement shown here renames the function make_pizza() to mp()
# in this program. Any time we want to call make_pizza() we can simply write
# mp() instead, and python will run the code in make_pizza()

# the general syntax for providing an alias is:
# from module_name import function_name as fn