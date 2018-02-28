from random import randint
class Die():
    def __init__(self):
        self.sides=6
    def roll_die(self,sides):
        self.sides=sides
        guess=randint(0,self.sides)
        print(guess)
roll_six_die=Die()
#for i in range(10):
#    roll_six_die.roll_die(6)
roll_ten_die=Die()
for i in range(10):
    roll_ten_die.roll_die(10)

