'''uniform
random.uniform(a, b)

返回一个随机浮点数 N
当 a <= b 时 a <= N <= b
当 b < a 时 b <= N <= a

取决于等式 a + (b-a) * random() 中的浮点舍入
终点 b 可以包括或不包括在该范围内
'''

import random

print(random.uniform(1, 2))
print(random.uniform(3, 2))
