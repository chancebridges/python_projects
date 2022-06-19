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
    