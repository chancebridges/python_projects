from user import User

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
