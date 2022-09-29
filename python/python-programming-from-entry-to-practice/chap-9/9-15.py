# -*- coding: utf-8 -*-

from random import randint


class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides - 1))


die = Die()
for n in range(1, 11):
    die.roll_die()

print('---' * 12)


class Die_10(Die):

    def __init__(self, sides):
        super().__init__(sides)


die_10 = Die_10(10)
for n in range(1, 11):
    die_10.roll_die()

print('---' * 12)


class Die_20(Die):

    def __init__(self, sides):
        super().__init__(sides)


die_20 = Die_20(20)
for n in range(1, 11):
    die_20.roll_die()
