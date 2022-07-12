# you can also provide an alias for a module name. Giving a module a short
# alias like p for pizza, allows you to call the module's function's
# more quickely. 

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# the module pizza is given the alias p in the import statement, but all of
# the module's functions retain their original names. 

# the general syntax for this approach is:
# import module_name as mn