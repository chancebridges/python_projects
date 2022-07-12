class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        
        Employee.num_of_emps +=1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    @classmethod 
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    # by doing this we pass the class as the first argument instead of the instance. 
    # the common convention for class variables is cls
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # this line will create the new employee

    @staticmethod
    def is_workday(day):
        if day.weekday() ==5 or day.weekday() ==6:
            return False
        return True
        
    # a giveaway if a method should be static would be if you do not access it.
        
emp_1 = Employee('Chance', 'Bridges', 85000)
emp_2 = Employee('Test', 'Employee', 50000)


# in python monday is equal to 0, sunday = 6

#Employee.set_raise_amt(1.05)
# when modifying a class variable it will change it in the class which will
# also change it for the instances calling on the class.

#print(Employee.raise_amt)
#print(emp_1.raise_amt)
#print(emp_2.raise_amt)

# regular methods automatically takes in the instance as the first argument.

#line emp_str_1 thorugh print(new_emp_1.pay) for classmethod.
#emp_str_1 = 'John-Doe-70000'
#emp_str_2 = 'Steve-Smith-30000'
#emp_str_3 = 'Jane-Doe-90000'

#new_emp_1 = Employee.from_string(emp_str_1)

#print(new_emp_1.email)
#print(new_emp_1.pay)

# static methods do not pass anything automatically, the instance or class