from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# importing classes is an efective way to program. 
# you still get all the same functionality, but you keep your main program
# files clean and easy to read. 