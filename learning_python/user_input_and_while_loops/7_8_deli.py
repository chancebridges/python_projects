sandwich_orders = ['pepperoni', 'banana peppers', 'ranch']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I want a " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print("Each sandwich has been made. ")
print(finished_sandwiches)