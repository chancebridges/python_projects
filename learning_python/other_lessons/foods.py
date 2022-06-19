my_numbers = ['alpha', 'beta', 'gamma']
friends_numbers = my_numbers[:]

print("my favorite numbers are:")
print(my_numbers)

print("\nMy friend's favorite numbers are:")
print(friends_numbers)

my_numbers.append('delta')
friends_numbers.append('epsilon')

print(my_numbers)
print(friends_numbers)

# you must use a slice when copying lists, if you do not add [:] then it will be linked to the old list


