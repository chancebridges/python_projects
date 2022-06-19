# The keys() method is useful when you dont need to work with all
# of the values in a dictionary. 
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

for name in favorite_languages.keys():
    print(name.title())
# line 10 tells python to pull all the keys from the dictionary and store them
# one at a time in the variable name. 

# looping through the keys in the default behavior when looping through the dictionary

# this code for line 10 could have been " for name in favorite_languages: "
# and it would have given the same result. 