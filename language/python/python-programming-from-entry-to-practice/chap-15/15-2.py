# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cubes = [val**3 for val in input_values]

plt.scatter(
    input_values, cubes, c=input_values, cmap=plt.cm.Blues, edgecolors='none', s=7
)
plt.title('Cube Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()
