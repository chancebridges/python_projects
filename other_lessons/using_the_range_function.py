# you can use the range() function to print a series of numbers
# range() fnuction never contains the end value you input

for value in range(1,5):
    print(value)
print("\n")

for value in range(1,6):
    print(value)
print("\n")

#Using range() to make a list of numbers

numbers = list(range(1,6))
print(numbers)

# How to skip numbers in a given range

even_numbers = list(range(2,11,2))
print(even_numbers)

# How to do squares using the range function

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# another way to do squares using the range function

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

# simlpe statistics with a list of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(str(min(digits))+ "\n")
print(str(max(digits)) + "\n")
print(str(sum(digits)) + "\n")

# List comprehension

squares = [value**2 for value in range(1,11)]
print(squares)

