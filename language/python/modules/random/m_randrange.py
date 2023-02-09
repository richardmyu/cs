'''randrange
random.randrange(stop)
random.randrange(start, stop[, step])

返回一个随机选择的元素。
这相当于 choice(range(start, stop, step)) ，
但实际上并没有构建一个 range 对象。
'''

import random

print(random.randrange(13))

print(random.randrange(1, 13))

print(random.randrange(1, 13, 2))
