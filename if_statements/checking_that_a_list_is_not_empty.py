# it can be useful to check whether a list is empty before running a for loop

requested_toppings = []
# the list above is empty
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# when using the name of a list in an if statement, python returns true if
# the list contains at least one item. an empty list evaluates to false. 
#if the test is true, we use the for loop. if the test fails we use the else line

