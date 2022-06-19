# use the keys() method to find out if a particular value is not 
# a key in a dictionary

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# the keys() method isnt just for looping: it actually returns a list
# of all the keys. 