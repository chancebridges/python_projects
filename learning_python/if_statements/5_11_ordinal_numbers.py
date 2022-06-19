numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for number in numbers:
    if int(number) < 2:
        print("\n" + str(number) + "st.")
    elif int(number) < 3:
        print("\n" + str(number) + "nd.")
    elif int(number) < 4:
        print("\n" + str(number) + "rd.")
    else:
        print("\n" + str(number) + "th.")
