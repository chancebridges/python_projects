people = []

bob = {
    'first_name': 'bob',
    'last_name': 'ford',
    'age': 24 ,
    'city': 'marion',
}

maximus = {
    'first_name' : 'maximus',
    'last_name' : 'gladiator',
    'age' : 30 ,
    'city' : 'rome'
}

leonidas = {
    'first_name' : 'leonidas',
    'last_name' : 'leo',
    'age' : 38,
    'city' : 'sparta'
}

people.append(bob)
people.append(maximus)
people.append(leonidas)

for person in people:
    print(person['first_name'] + ": " +str(person))