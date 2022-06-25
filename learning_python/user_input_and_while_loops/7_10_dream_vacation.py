print("Where would your dream vacation take place? ")
poll = {}
poll_active = True

while poll_active:
    name = input("Please enter your name: ")
    location = input("Where would you go?: ")
    poll[name] = location 
    print(name + " would like to go on vaction to " + location + ".")
    
    print("Would you like to enter another name? ")
    answer = input("yes or no: ")
    if answer == 'no':
        poll_active = False
for name, location in poll.items():
    print(name + "would like to go to " + location + ".")