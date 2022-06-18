# Simple calculator
# Areas for improvement
# 1. Extend to accept floats instead of just int
# 2. Don't exit after first operation, allow for several 
# 3. Add tests

print("Command Line Calculator")
print("------------------------")
print("Supports 'add', 'subtract', 'multiply' ")
print(" 'divide', 'square' and 'exponent'. ")

valid_operators = ['add', 'subtract', 'multiply', 'divide', 'square', 'exponent']

def main():

    operator = ""
    while True:
        operator = input("Enter an operator: ")
        if operator in valid_operators:
            break
        print("Enter a valid operator.")

    operand_1 = ""
    while True:
        operand_1 = input("Enter first number: ")
        if operand_1.isnumeric():
            operand_1 = int(operand_1)
            break
        print("Enter a valid number.")

    if operator != "square":
        operand_2 = ""
        while True:
            operand_2 = input("Enter second number: ")
            if operand_2.isnumeric():
                operand_2 = int(operand_2)
                break
            print("Enter a valid number.")

    print("Result: ", end='')
    if operator == "add":
        print(operand_1 + operand_2)
    elif operator == "subtract":
        print(operand_1 - operand_2)
    elif operator == "multiply":
        print(operand_1 * operand_2)
    elif operator == "divide":
        print(operand_1 / operand_2)
    elif operator == "square":
        print(operand_1 ** 2)
    elif operator == "exponent":
        print(operand_1 ** operand_2)
    else:
        print(operand_1 + operand_2)

if __name__ == "__main__":
    main()