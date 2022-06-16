# Sorting a list permanently with the sort() method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sort(reverse=True) sorts a list in reverse alphabetical order

cars.sort(reverse=True)
print(cars)


# Sorting a list temporarily with the sorted function

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted line:")
print(sorted(cars))

# you can also reverse the sorted method

print("\nHere is the reversed sorted list")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

# printing a list in reverse order
# you can use the reverse() method to reverse the original order of a list
print("\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# the reverse method changes the order of a list permanently, you can revert to 
# the original order anytime by applying reverse() again

# finding the length of a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
