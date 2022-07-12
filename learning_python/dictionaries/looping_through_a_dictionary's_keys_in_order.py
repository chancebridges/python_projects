# a dictionary always maintains a clear connection between each key and its 
# associated value, but you never get the items from a dictionary in any 
# predictable order. 

# one way to return items in a certain order is to sort the keys
# as they're returned in the for loop. You can use the sorted() function to 
# get a copy of the keys in order

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# this for statement is like any other for statements, except we've wrapped
# the sorted() function around the dictionary.keys() method