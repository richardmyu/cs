# -*- coding: utf-8 -*-

from random import randint
import time
import pygal


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die_1 = Die(8)
die_2 = Die(8)
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = 'Results of rolling a D8 * 2 1000 times.'
hist.x_labels = [str(val) for val in range(2, max_result + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D8 + D8', frequencies)
hist.render_to_file(f'dice_visual_{time.time()}.svg')
