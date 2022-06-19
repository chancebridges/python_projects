cities = {
   'marion' : {
    'country' : 'United States of America',
    'population' :27730,
    'fact' : 'Marion has the largest private school in Indiana'
   } ,
   'muncie' : {
    'country' : 'United States of America',
    'population' : 67739,
    'fact' : 'Home of ball state university'
   },
   'kokomo' : {
    'country' : 'United States of America',
    'population' : 58066,
    'fact' : 'known as the city of firsts'
   }

}

for key, value in cities.items():
    print(key + ": " +str(value))