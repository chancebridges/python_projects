print("Please input one of the following: ")
print("add, subtract, multiply, divide, square")
print("if doing a square, the first number will be used.")

kind = input("What would you like to do? ")
num_1 = input("first number: ")
num_2 = input("second number: ")

number_1 = int(num_1)
number_2 = int(num_2)

if kind == "add":
    print(number_1 + number_2)
if kind == "subtract":
    print(number_1 - number_2)
if kind == "multiply":
    print(number_1 * number_2)
if kind == "divide":
    print(number_1 / number_2)
if kind == "square":
    print(number_1 ** 2)
