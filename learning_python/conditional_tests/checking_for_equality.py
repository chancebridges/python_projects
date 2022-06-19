car = 'bmw'
print(car == 'bmw')

# Think of a single equal sign as a statement "set the value of car equal 
#to 'audi'".
# Think of a double equal sign as asking a question: " is the value of car 
# equal to 'bmw'?"

# two values with different capitalization are not considered equal:

car = 'Audi'
print(car=='audi')

# you can convert the variable's value to lowercase before doing the comparison
car = 'Audi'
print(car.lower() == 'audi')

# the lower() function does not change the value that was originally stored
# in car, so you can do this kind of comparison without affecting the original value

print(car)