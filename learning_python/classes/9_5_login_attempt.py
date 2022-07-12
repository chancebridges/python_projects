class User:
    def __init__(self, first_name, last_name, age, sex, height, login_attempts=0):
        """Represent a users information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.height = height
        self.login_attempts = login_attempts
        
    def describe_user(self):
        print("The users name is " 
        + self.first_name.title() + self.last_name.title()
        + " and they are " + str(self.age) + " years old."
        + " They are a " + self.sex + ". They are " + str(height) + " tall.")
    
    def greet_user(self): 
        print(f'Hello {self.first_name.title()} {self.last_name.title()}')
        
    def increment_login_attempts(self):
       self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user_1 = User('chance', 'bridges', 24, 'male', "5'8")

user_1.greet_user()
User.greet_user(user_1)
User.increment_login_attempts(user_1)
User.increment_login_attempts(user_1)
User.increment_login_attempts(user_1)
User.increment_login_attempts(user_1)
print(user_1.login_attempts)
User.reset_login_attempts(user_1)
print(user_1.login_attempts)