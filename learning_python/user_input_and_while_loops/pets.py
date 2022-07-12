pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# we start with a list of multiple instances of a value, after printing the 
# list, python enters the while loop. once inside the loop, python removes the
# first instance of the value and then returns to the while line and continues
# this cycle until the value is no longer in the list. 