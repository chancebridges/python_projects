class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        return '{} {}'.format(self.first, self.last)



# if you have a class that you want to leave empty for the time being, you
# can enter a pass statement and python will know to skip that for now

# A class is basically a blueprint for an isntance of a class

emp_1 = Employee('chance', 'bridges', '80000')
emp_2 = Employee('Test', 'User', 60000)

print(Employee.full_name(emp_1))
print(emp_1.full_name())
