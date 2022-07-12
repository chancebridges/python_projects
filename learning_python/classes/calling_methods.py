class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# after we create an instance from the class Dog, we can use the dot
# notation to call any method defined in Dog. 

my_dog.sit()
my_dog.roll_over()

# to call a method, give the name of the instance ( in this case, my_dog)
# and the method you want to call, separated by a dot. When python reads 
# my_dog.sit(), it looks for the method sit() in the class Dog and runs
# that code. 