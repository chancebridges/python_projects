# if you need to evaluate more than two possible situations you can use pythons
# if-elif-else syntax. python executes only one block in an if-elif-else chain
# refer to amusement_park.py

age = int(input("Please enter your age here: "))

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")
