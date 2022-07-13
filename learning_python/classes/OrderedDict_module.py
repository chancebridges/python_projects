from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages is " +
        language.title() + '.')
        

# Instances of the OrderedDict class behave almost exactly like dictionaries
# except they keep track of the order in which key-value pairs are added. 

