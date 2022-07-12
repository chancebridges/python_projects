# When modeling something from the real world in code, you may find that 
# you're adding more and more detail to a class. You will find that your have
# a growing list of attributes and methods and that your files are becoming
# lengthy. 

# You can break your large class into smaller classes that work together.

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

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + " -kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# at line 33 we define a new class called Battery that does not inherit from 
# any other class.

# The __init__() method at line 36 has one parameter, battery_saze, in 
# addition to self. This is an optional parameter that sets the battery's
# size to 70 if no value is provided. 

# In line 53 we add an attribute called self.battery. This line tells Python
# to create a new instance of Battery (with a default size of 70) and store 
# that instance in the attribute self.battery

# line 53 tells python to look at the instance my_tesla, find its battery 
# attribute, and call the method describe_batery() that's associated with the 
# Battery instance stored in the attribute. 