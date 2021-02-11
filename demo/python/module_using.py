# -*- coding: utf-8 -*-

import sys

# 每一个 Python 模块都定义了各自的 __name__。
# 如果其值为 '__main__'，这说明用户正在单独运行这个模块


print("The command line arguments are: ")

# sys.argv 命令行参数列表
for i in sys.argv:
    print(i)

# sys.path 是模块导入时要搜索的目录列表
print("\n\nThe PYTHONPATH is ", sys.path, "\n")


def say_hi():
    if __name__ == '__main__':
        print('This program is being run by itself')
    else:
        print('I am being imported from another module')


__version__ = '0.1'
