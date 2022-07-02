# if the name of a function you're importing might conflickt with an existing
# name in your program, or if the function name is long, you can use a short
# unique alias. 

# below we give the funcitonmake_pizza() an alias, mp(), by importing
# make_pizza as mp. the keyword renames a function using the alias you provide:

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')