class User():
    def __init__(self, first_name, last_name, age, sex, height):
        """Represent a users information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.height = height
        
    def describe_user(self):
        print("The users name is " 
        + self.first_name.title() + self.last_name.title()
        + " and they are " + str(self.age) + " years old."
        + " They are a " + self.sex + ". They are " + str(height) + " tall.")
    
    def greet_user(self): 
        print(f'Hello {self.first_name.title()} {self.last_name.title()}')
        
    def __str__(self):
        return self.first_name
        
    def __len__(self):
        return (len(self.first_name))
        
class Privelage():
    def __init__(self, privelages='priv'):
        self.privelages = privelages

    def show_privelages(self):
        if self.privelages == 'priv':
            priv_1 = "can add post"
            priv_2 = "can delete post"
            priv_3 = "can ban user"
            print("the admins privelages include: \n" + priv_1 + 
            "\n" + priv_2 + "\n" + priv_3)
        else:
            print('no')
        
class Admin(User):
    def __init__(self, first_name, last_name, age, sex, height, privs):
        super().__init__(first_name, last_name, age, sex, height)
        self.privelages = Privelage()
