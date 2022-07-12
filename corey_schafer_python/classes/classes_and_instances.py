class Employee:
    
    def __init__(self, first, last, pay):
        # think of the __init__() function as initialize

        # when you create methods in a class they receive the first instance
        # as the first argument automatically, and by convention this is named 
        # self.
        self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        return '{} {}'.format(self.fname, self.last)



# if you have a class that you want to leave empty for the time being, you
# can enter a pass statement and python will know to skip that for now

# A class is basically a blueprint for an instance of a class

emp_1 = Employee('chance', 'bridges', '80000')
# The instance is passed automatically so you do not need to input it.
# For example line 24 will pass 'emp_1' to 'self' in the class 
emp_2 = Employee('Test', 'User', 60000)

# line 19 and 20 are considered instances of the class Employee

# below are two ways to call on class functions
print(emp_1.email)
print(Employee.full_name(emp_1))
print(emp_1.full_name())
print(emp_2.full_name())

# an instance variable contains data which is unique to each variable. 