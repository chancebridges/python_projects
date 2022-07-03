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

# a function thats part of a class is a method

# everything you learned about functions applies to methods as well, the only
# practical difference for now is the way we'll call methods. 

# the __init__() method at line 4 is a special method that python runs whenever
# we create a new instance based on the Dog class.

# The __init__() method has two leading underscores and two trailing underscores
# , a convention that helps prevent pythons default method names from 
# conflicting with your method names.

# the self parameter is required in the method definition, and it must come 
# before the other parameters. It must be inclided in the definition becuase 
# when python calls this __init__() method later, the method call will 
# automatically pass the self argument. 

# every method call associated with a class automatically passes self, which
# is a reference to the instance itself. it gives the individual instance
# access to the attributes and methods in the class. 

# any variable prefixed with self is available to every method in the class, 
# and we'll also be able to access these variables through any instance 
# created from the class. 

# variables that are accessible through instances like this are called attributes.

