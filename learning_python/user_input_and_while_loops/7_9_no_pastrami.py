sandwich_orders = ['pastrami','pepperoni', 'pastrami', 'banana peppers', 'pastrami', 'ranch']
finished_sandwiches = []

print("We are out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I want a " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print("Each sandwich has been made. ")
print(finished_sandwiches)