# how to change values in a list

motorcycles = [ 'honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# the code at line 4 changes the value of the first item to ducati

# how to add elements to a list
# the simplist way to add a new element to a list is to append the item to the list

motorcycles.append('ducati')
print(motorcycles)

# the append() method makes it easy to build lists dynamically

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# how to insert elements into a list

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)
# when inserting an element into the list it shifts every other value in the list one position to the right

# how to remove elements using the del statement

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# when using the del method you will no longer be able to access the value that was removed


