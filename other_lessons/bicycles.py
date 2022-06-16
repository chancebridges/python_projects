# a list is a collection of items in a particular order
# in python, square brackets [ ] indicate a list, individual elements in the list are separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# to access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets
print(bicycles[0])
print("\n" + bicycles[0].title())

# python consideres the first item in a list to be at position 0, not position 1

print(bicycles[1] + " " + bicycles[3])

# by asking for the item at index -1, python always returns the last item in the list
print(bicycles[-1])

# this convention extends to other negative index values. Ex. -2 = redline

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
