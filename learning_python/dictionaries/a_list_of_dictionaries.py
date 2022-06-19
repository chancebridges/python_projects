# nesting: storing a set of dictionaries
# in a list or a list of items as a value in a dictionary.

# you can nest a set of dictionaries inside a list, a list of 
# items inside a dictionary, or even a dictionary inside another dictionary.

# see aliens.py


# make an empty list for storing aliens.
aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green' , 'points' : 5 , 'speed': 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# at line 14 the range() returns a set of numbers, which just tells python
# how many times we want the loop to repeat.

# how could we make some of the aliens faster? Python considers each to be a 
# separate object, which allows us to work with each alien individually.

print("-------------------------")

aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green' , 'points' : 5 , 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

