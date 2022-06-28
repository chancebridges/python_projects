def city_country(city, country):
    """Displays a city and country"""
    print(city.title() + ", " + country.upper())

city_country('marion', 'usa')
city_country(city='Nashville', country='usa')
city_country(country='usa', city='kokomo')