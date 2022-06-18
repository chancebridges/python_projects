# when you no longer need a piece of information thats stored in a dictionary, 
# you can use the del statement to completely remove a key-value pair
# all del needs is the name of the dictionary and the key that you want to remove

alien_0 = {'color' : 'green' , 'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# be aware that the deleted key-value pair is removed permanently
