'''gammavariate
random.gammavariate(alpha, beta)

Gamma 分布。不是 gamma 函数！
参数的条件是 alpha > 0 和 beta > 0

'''

import random

print(random.gammavariate(1 / 100, 1 / 100))
print(random.gammavariate(1, 1))
print(random.gammavariate(100, 100))
