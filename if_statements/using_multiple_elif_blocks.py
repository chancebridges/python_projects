# you can use as many elif blocks in your code as you like

age = 64

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# the second elif block at line 9 now checks to make sure a person is less than
# age 65 before assigning them the full admission rate of $10. 

print("\n")
print("below is an example without the else block.")

# python does not require an else block at the end of an if-elif chain.
# look below for an example not using an else block

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age > 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")