# If you are primarily interested in the values that a dictionary contains, 
# you can use the values() method to return a list of values without keys

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# the for statemnt on line 12 pulls each value from the dictionary and
# stores it in the variable language.

# to see each value without repetition, we can use a 'set'.
# a set is similar to a list except that each item in the set must be unique.


print("\n\n")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# when you wrap set() around a list that contains duplicate items, python 
# identifies the unique items in a list and builds a set from those items.