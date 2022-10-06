# -*- coding: utf-8 -*-

import time
import pygal
from die import Die

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

# 结果可视化
hist = pygal.Bar()
hist.title = 'Results of rolling two D6 dice 10000 times.'
hist.x_labels = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
    '16'
]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file(f'different_die_visual_{time.time()}.svg')
