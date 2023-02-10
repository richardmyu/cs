'''sample
random.sample(population, k, *, counts=None)

返回包含来自总体的元素的新列表，同时保持原始总体不变
结果列表按选择顺序排列，因此所有子切片也将是有效的随机样本

总体成员不必是 hashable 或 unique
如果总体包含重复，则每次出现都是样本中可能的选择

重复的元素可以一个个地直接列出
或使用可选的仅限关键字形参 counts 来指定
例如，sample(['red', 'blue'], counts=[4, 2], k=5)
等价于
sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)。

要从一系列整数中选择样本
请使用 range() 对象作为参数
对于从大量人群中采样
这种方法特别快速且节省空间
sample(range(10000000), k=60)

如果样本大小大于总体大小
则引发 ValueError
'''

import random

ll_1 = [1, 2, 3, 4]
ll_2 = [1, 2, 3, 4, 4, 4, 4]

print(random.sample(ll_1, k=4))
print(ll_1)

print(random.sample(ll_2, k=4))
print(ll_2)

print(random.sample(['tens', 'low cards'], counts=[16, 36], k=20))
