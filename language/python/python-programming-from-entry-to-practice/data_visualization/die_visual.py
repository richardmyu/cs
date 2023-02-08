import time
import pygal
from die import Die

die = Die()
results = []

for roll_num in range(50000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []

for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

# 结果可视化
hist = pygal.Bar()
hist.title = 'Results of rolling one D6 5000 times.'
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_labels = [str(val) for val in range(1, 7)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6', frequencies)
hist.render_to_file(f'die_visual_{time.time()}.svg')
