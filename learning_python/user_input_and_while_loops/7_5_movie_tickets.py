print("Please enter your age for the price of the ticket ")
print("Enter quit to end program.")
age = ""

while age != 'quit':
    age = input("age: " )
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3 :
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")