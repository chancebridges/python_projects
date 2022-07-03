class Restaurant():
    """A simple attempt to describe a resturaunt."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine type."""
        self.name = restaurant_name
        self.type = cuisine_type
    def describe_restaurant(self):
        """describes the restaurant."""
        print(self.name.title() + " is a large chain restaurant.")
        print(self.name.title() + " has been in business for 50 years.")
    def open_restaurant(self):
        print("The restaurant is open!")

fave_restaurant = Restaurant('fazolis', 'pasta')
print("My favorite restaurant is " + fave_restaurant.name.title())
print("My favorite restaurant's cuisine type is " + fave_restaurant.type)
fave_restaurant.describe_restaurant()
fave_restaurant.open_restaurant()

print("\n")

fave_restaurant_2 = Restaurant('mcdonalds', 'fast food')
fave_restaurant_2.describe_restaurant()

print("\n")

fave_restaurant_3 = Restaurant('Texas Roadhouse','Steak')
fave_restaurant_3.describe_restaurant()