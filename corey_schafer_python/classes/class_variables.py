class Employee:

    num_of_emps = 0
    raise_amount = 1.04
    
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Chance', 'Bridges', 85000)
emp_2 = Employee('Test', 'User', 50000)

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)
# Class variables should be the same for each instance. 

#The following line is how you would change the value for the entire class
#Employee.raise_amount = 1.05

#The following is how you would change the value for just one instance
#emp_1.raise_amount = 1.05

# The following are ways to access raise_amount
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

#To see what is in a class use the __dict__ modifier
#print(Employee.__dict__)

print(Employee.num_of_emps) # this counts emp_1 and emp_2. if you use this 
# before those lines of code, the result would be 0.