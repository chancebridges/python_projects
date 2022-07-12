class Restaurant():
    """A simple attempt to describe a resturaunt."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine type."""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served =int(0)

    def describe_restaurant(self):
        """describes the restaurant."""
        print(self.name.title() + " is a large chain restaurant.")
        print(self.name.title() + " has been in business for 50 years.")

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, number):
        self.number_served = str(number)
        print("The number served is " + self.number_served)
    
    def increment_number_served(self, increment):
        self.number_served = int(increment) + int(self.number_served)
        print("The number served is " + str(self.number_served))

fave_restaurant = Restaurant('fazolis', 'pasta')
print("My favorite restaurant is " + fave_restaurant.name.title())
print("My favorite restaurant's cuisine type is " + fave_restaurant.type)
fave_restaurant.describe_restaurant()
fave_restaurant.open_restaurant()

restaurant = Restaurant('mcdonalds', 'fries')
print(str(restaurant.number_served))
restaurant.number_served = 50
print(str(restaurant.number_served))

restaurant.set_number_served(50)
restaurant.increment_number_served(int(2))
