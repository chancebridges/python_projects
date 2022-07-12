# once you have a child class that inherits from a parent class, you can add
# any new attributes and methods necessary to differentiate the child class 
# from the parent class. 

# lets add an attribute thats specific to electric cars.

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a "+  str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
#print(my_tesla.get_descriptive_name())
print(ElectricCar.get_descriptive_name(my_tesla))
my_tesla.describe_battery()

# at line 41 we add a new attribute and set its initial value. This attribute
# will be associated with all instances created from the ElectricCar class,
# won't be associated with any instances of Car. 

# at line 43 we add a method describing information about the battery.

# There's no limit to how much you can specialize a subclass.

# you can add as many attributes and methods as you need to whatever degree 
# of accuracy you need.

# an attribute or method that could belong to any car, rather than one 
# specific to an electric car should be added to the Car class instead of
# the ElectricCar class. 