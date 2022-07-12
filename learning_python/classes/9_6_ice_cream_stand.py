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

class Ice_Cream_Stand(Restaurant):
    """A simple way to describe an ice cream stand."""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Describe the ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print(f"The flavors of ice cream we serve are:" "\nChocolate" "\nVanilla" "\nStrawberry")

big_dipper = Ice_Cream_Stand('big dipper', 'ice cream','chocolate, vanilla, strawberry')
Ice_Cream_Stand.display_flavors(big_dipper)