from random import randint

class Dice:
  """A simple attempt to model a die and roll it to get a random number"""
  def __init__(self , die_side = 6):
    """Initialize attributes to describe a die \n In this case we have only one attribute die_side"""
    self.die_side = die_side
  def roll_die(self):
    """Simulate rolling a die and return points based on the side of the die rolled"""
    return randint(1 , self.die_side)

my_six_sided_die = Dice()
my_ten_sided_die = Dice(10)
my_twenty_sided_die = Dice(10)

print("Rolling a 6 sided die")
for i in range (10) :
  print(my_six_sided_die.roll_die())

print("Rolling a 10 sided die")

for i in range (10) :
  print(my_ten_sided_die.roll_die())

print("Rolling a 20 sided die")

for i in range (10) :
  print(my_twenty_sided_die.roll_die())


