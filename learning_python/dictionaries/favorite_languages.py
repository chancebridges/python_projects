favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
# looping through all key-value pairs works particularly well for dictionaries
# if you loop through a dictionary you get the name of the key and the name of the value

# for key, value in 'dictionary name'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
     language.title() + ".")