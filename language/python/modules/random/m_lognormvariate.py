'''lognormvariate
random.lognormvariate(mu, sigma)

对数正态分布
如果你采用这个分布的自然对数
你将得到一个正态分布
平均值为 mu 和标准差为 sigma
mu 可以是任何值，sigma 必须大于零
'''

import random

print(random.lognormvariate(2, 0.1))
