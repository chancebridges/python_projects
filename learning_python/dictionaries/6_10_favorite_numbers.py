favorite_numbers = {
    'alpha' : [1, 2, 3] ,
    'beta' : [2, 3, 4],
    'gamma' : [3, 4, 5],
    'delta' : [4, 5, 6],
    'epsilon' : [5, 6, 7]
    }

for key, value in favorite_numbers.items():
    print(key + "'s favorite numbers are: " + str(value))