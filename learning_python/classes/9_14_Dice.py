from random import randint

class Die():
    """Represents a die"""
    def __init__(self, sides=6):
        """Represents a six sided die"""
        self.sides = sides
        
    def roll_die(self):
        """rolls the die to give a random number between 1 and 6"""
        if self.sides == 6:
            x = randint(1,6)
        elif self.sides ==10:
            x = randint(1,10)
        elif self.sides ==20:
            x = randint(1,20)
        roll = (print(x))    
        return roll 
         
    def repeat_roll(self):
        """Repeats the roll_die method 10 times."""      
        for x in range(0,10):
            if self.sides == 6:
                six_die_roll.roll_die()
            elif self.sides == 10:
                ten_sided_die_roll.roll_die()
            elif self.sides == 20:
                twenty_sided_die_roll.roll_die()

print("six sided rolls")             
six_die_roll = Die(6)
six_die_roll.repeat_roll()

print("ten sided rolls")
ten_sided_die_roll = Die(10)
ten_sided_die_roll.repeat_roll()

print("twenty sided rolls")
twenty_sided_die_roll = Die(20)
twenty_sided_die_roll.repeat_roll()