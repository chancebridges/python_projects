user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi' ,
}

# create names for the two variables that will hold 
# the key and value in each key-value pair.
# The for loop then stores each of these pairs in the two variables provided.
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# the method .items() returns a list of key-value pairs