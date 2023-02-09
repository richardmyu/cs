'''seed
random.seed(a=None, version=2)

初始化随机数生成器
可以在调用其他随机模块函数之前调用此函数
'''

import random

random.seed()
print("使用默认种子生成随机数：", random.random())
print("使用默认种子生成随机数：", random.random())

random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())

random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())
