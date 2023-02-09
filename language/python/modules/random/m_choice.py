'''choice
random.choice(seq)

从非空序列 seq 返回一个随机元素
如果 seq 为空，则引发 IndexError
'''

import random

print(random.choice([1, 2, 3, 4]))
print(random.choice([1, 2, 3, 4, 4, 4]))
