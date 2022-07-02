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

# at line 18 we tell python to create a dog whose name is 'willie' and whose
# age is 6. When python reads this line it calls the __init__() method
# in Dog with the arguments 'willie' and 6. the __init__() method creates an
# instance representing this particular dog and sets the name and age 
# attributes using the values we provided. 

# the __init__() method has no exploicit return statement, but python 
# automatically returns an instance representing this dog. 