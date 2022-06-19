favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

friends = ['phil' , 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + 
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

# at line 8 we make a list of friends that we want to print a message to.
# at line 12 we check to see if the name is in the list friends

