# You can override any method from the parent class that does not fit what
# what you're trying to model. To do this, you define a method in the child
# class with the same name as the method you want to override in the parent
# class. Python will disregard the parent class method and only pay attention 
# to the method you define in the child class. 

# Say the class Car had a method called fill_gas_tank(), we could override it
# with the following edit


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

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
# my_tesla.fill_gas_tank()
ElectricCar.fill_gas_tank(my_tesla)

# now if someone tries to call fill_gas_tank() with an electric car, python
# will ignore the method fill_gas_tank() in Car and run this code instead.

# When you use inheritance, you can make your child classes retain what you 
# need and override anything you don't need from the parent class.