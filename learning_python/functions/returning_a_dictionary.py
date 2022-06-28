# a function can return any kind of value you need it to, including more complicated
# data structures like lists and dictionaries

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hednrix', age=27)
print(musician)

# the function build_person() takes in a furst and last name, and packs these
# values into a dictionary at line 6.

# the entire dictionary repesenting the person is returned at line 7

# the return value is printed at line 10, with the two original pieces of 
# textual info now stored in a dictionary.

