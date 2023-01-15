# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import time
from random import choice


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


rw = RandomWalk(5000)
rw.fill_walk()

plt.figure(figsize=(10, 6))

point_numbers = list(range(rw.num_points))

plt.scatter(rw.x_values, rw.y_values, edgecolors='none', s=1)
# plt.plot(rw.x_values, rw.y_values, linewidth=1)
plt.scatter(0, 0, c='green', edgecolors='none', s=10)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10)
plt.show()
