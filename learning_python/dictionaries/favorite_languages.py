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

# the code at line 11 tells pytohn to loop through each key-value pair in the dictionary

print("\n")

favorite_languages = {
    'jen' : ['python','ruby'],
    'sarah' :['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(language) > 2:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
                print("\t" + language.title())
    if len(language) < 2:
        print("\n" + name.title() + "'s favorite language is:")
        for language in languages:
            print("\t" + language.title())