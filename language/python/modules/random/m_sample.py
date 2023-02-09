'''sample
random.sample(population, k, *, counts=None)

返回包含来自总体的元素的新列表，同时保持原始总体不变
结果列表按选择顺序排列，因此所有子切片也将是有效的随机样本

总体成员不必是 hashable 或 unique
如果总体包含重复，则每次出现都是样本中可能的选择
'''

import random

ll_1 = [1, 2, 3, 4]
ll_2 = [1, 2, 3, 4, 4, 4, 4]

print(random.sample(ll_1, k=4))
print(ll_1)

print(random.sample(ll_2, k=4))
print(ll_2)
