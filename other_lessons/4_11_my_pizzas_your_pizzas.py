pizzas = ['pepperoni', 'sausage', 'cheese']
for pizza in pizzas:
    print(pizza)
    print("I like " + pizza + " pizza!" + "\n")
print("I really love pizza!")

print("\n")

friend_pizzas = pizzas[:]
pizzas.append('meat lovers')
friend_pizzas.append('supreme')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print("\n")

print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)