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

# notice there are no curly brackets at line 3, the call to OrderedDict()
# creates an empty ordered dictionary for us and stores 
# it in favorite_languages.

# This is a great class to be aware of because it combines the main 
# benefit of lists(retaining your original order) with the main feature
# of dictionaries (connecting pieces of information).

# You can also download modules from external sources. 