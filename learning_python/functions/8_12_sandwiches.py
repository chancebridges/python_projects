def sandwiches(*items):
    """ creates a list of sandwich ingredients"""
    for i in items:
        topp = str(i)
        print("\nI would like the following items on my sandwich: ")
        print(" - " + topp)

toppings = ['jelly', 'peanut butter']
toppings_2 = ['butter, cinnamon, toast']
toppings_3 = ['egg']
sandwiches(toppings)
sandwiches(toppings_2)
sandwiches(toppings_3)