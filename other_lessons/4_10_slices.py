players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:])
print(players[:2])
print(players[-3:])

numbers = ['alpha', 'beta', 'gamma', 'delta']
for number in numbers[1:3]:
    print(number.title())


print("The first three items in the list are:")
print(players[0:3])

print("Three items from the middle of the list are:")
print(players[1:4])

print("The last three items in the list are:")
print(players[-3:])
