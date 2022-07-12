# Every attribute in a class needs an initial value, even if that value is 
# zero or an empty string. In some cases, such as when setting a default value,
# it makes sense to specify this initial value in the body of the __init__()
# method. 

# lets add an attribute called odometer_reading that always starts with a value
# of zero.

class Car():

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# This time when python calls the __init__() method to create a new instance, 
# it stores the make model and year values as it did before. Then it creates
# a new attribute called odometer_reading and sets its initial value to 0

