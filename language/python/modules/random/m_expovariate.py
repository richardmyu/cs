'''expovariate
random.expovariate(lambd)

指数分布
lambd 是 1.0 除以所需的平均值，它应该是非零的。
（该参数本应命名为 “lambda” ，但这是 Python 中的保留字）
如果 lambd 为正，则返回值的范围为 0 到正无穷大
如果 lambd 为负，则返回值从负无穷大到 0
'''

import random

print(random.expovariate(1 / 100))

print(random.expovariate(-1 / 100))

print(random.expovariate(1))

print(random.expovariate(-1))

print(random.expovariate(100))

print(random.expovariate(-100))
