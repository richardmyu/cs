# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from random import randint
from random import choice
import time
import pygal


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


def matplotlib_die():
    die_1 = Die()
    die_2 = Die()
    die_3 = Die()
    results = []

    for roll_num in range(50000):
        result = die_1.roll() + die_2.roll() + die_3.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
    x_values = range(3, max_result + 1)

    for value in x_values:
        frequency = results.count(value)
        frequencies.append(frequency)

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, frequencies, linewidth=1)
    plt.show()


class RandomWalk:
    def __init__(self, num_points=50000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


def pygal_random_walk():
    rw = RandomWalk(5000)
    rw.fill_walk()

    hist = pygal.Bar()
    hist.title = 'Results of random walk 5000 times.'
    hist.x_labels = [str(val) for val in range(min(rw.x_values), max(rw.x_values) + 1)]
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'
    hist.add('random walk', rw.y_values)
    hist.render_to_file(f'15-10_dice_visual_{time.time()}.svg')


matplotlib_die()
pygal_random_walk()
