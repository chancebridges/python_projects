car = 'subaru'
print("is car == 'subaru'? I predict true.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print('\n')

house = 'marion'
print("Is house == 'Jonesboro'? I predict false" )
print(house == 'jonesboro')

print("\nIs house == 'marion'? I predict true")
print(house=='marion')

print('\n')

dog = 'oncie'
print("Is the dog != 'oncie'? I predict false")
print(dog != 'oncie')

print("\nIs the dog == 'oncie'? I predict true ")
print(dog == 'oncie')

print("\n")

spiderman = 'MaRvEl'
spider = spiderman.lower()
print("Is spiderman == 'marvel'? I predict true")
print(spider == 'marvel')

print("\nIs spiderman == 'dc'? I predict false")
print(spider == 'dc')

print("\n")

age = 24
print("Is my age == '21'? I predict false")
print (age ==21)
print("\n Is my age > '21'? I predict true" )
print (age > 21)
print("\nIs my age >= '21'? I predict true" )
print(age >= 21)
print("\nIs my age < '21'? I predict false ")
print(age < 21)
print("\nIs my age <= '21'? I predict false")
print(age <= 21)

new_age = 21
print("\n")
print("Is my age between twenty and thirty? I predict yes")
print(age >=20 and age <=30)

dogs = ['india', 'oncie', 'baisil', 'winston']
print("Is 'oncie' the name of one of our dogs?")
print('oncie' in dogs)
print("\nIs 'pedro' the name of one of our dogs?")
print('pedro' in dogs)

print("\n")

players = ['alpha', 'beta', 'gamma', 'delta']
new_player = 'epsilon'

if new_player not in players:
    print("Hello, " + new_player.title() + " you may enter your comment.")
