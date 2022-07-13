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