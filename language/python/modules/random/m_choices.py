'''choices
random.choices(population, weights=None, *, cum_weights=None, k=1)

从 population 中有重复地随机选取元素
返回大小为 k 的元素列表。
如果 population 为空，则引发 IndexError。
'''

import random

print(random.choices([1, 2, 3, 4], k=2))

print(random.choices([1, 2, 3, 4, 4, 4, 4], k=2))
