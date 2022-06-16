# the pop method removes the last item in a list but lets you work with that item after removing it

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print( "The last motorcycle I owned was a " + last_owned.title() + ".")


# How to pop an item from any position in a list
# include the index of the item you want to remove in parenthesis

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# remember that each time you use pop() the item you work with is no longer stored in the list

print(motorcycles)

# When you want to delete an item from a list and not use it in any way then use the del statement
# if you want to use an item as you remove it, use the pop() method


