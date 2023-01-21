# -*- coding: utf-8 -*-

import sys


def generator_expression():
    """生成式"""
    f = [x for x in range(1, 10)]
    print(f)

    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)

    f = [x**2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    # print(f)


def generator_function():
    """生成器"""
    f = (x**2 for x in range(1, 1000))
    print(sys.getsizeof(f))
    # print(f)

    # for val in f:
    #     print(val)


def generator_yield(n):
    """yield 生成器"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


if __name__ == '__main__':
    generator_expression()
    generator_function()

    for val in generator_yield(20):
        print(val)
