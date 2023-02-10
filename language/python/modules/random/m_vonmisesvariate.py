'''vonmisesvariate
random.vonmisesvariate(mu, kappa)

冯·米塞斯分布
mu 是平均角度，以弧度表示，介于0和 2*pi 之间
kappa 是浓度参数，必须大于或等于零
如果 kappa 等于零
则该分布在 0 到 2*pi 的范围内减小到均匀的随机角度。
'''

import random

print(random.vonmisesvariate(1, 2))
