rivers = {
    'nile' : 'egypt' ,
    'mississippi' : 'united states' ,
    'amazon' : 'south america'
}

for river, country in rivers.items():
    print("The " + river.title() + 
    " runs through " + country.title() + ".")

print("\n")

for river in rivers.keys():
    print("Then name of the river is: " + river.title())

print("\n")

for country in rivers.values():
    print("The location of the river is: " +
     country.title() + ".")