# lets write a new class representing a car. Our class will store information 
# about the kind of car we are working with.

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' '+ self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# at line 7 we define the __init__() method with the self parameter first, 
# just like we did before with our Dog class. 

# at line 13 we define a method called get_descriptive_name() that puts a 
# car's year, make, and model into one string neatly describing the car.

# at line 18 we make an instance from the Car class and store it in the 
# variable my_new_car.

