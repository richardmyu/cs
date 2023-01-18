# -*- coding: utf-8 -*-

import random
import math


def fn_1():
    a = 321
    b = 12
    print(a + b)  # 333
    print(a - b)  # 309
    print(a * b)  # 3852
    print(a / b)  # 26.75
    print(a // b)  # 26
    print(a % b)  # 9


def fn_2():
    a = 100
    b = 12.345
    c = 1 + 5j
    d = 'hello, world'
    e = True
    print(type(a))  # <class 'int'>
    print(type(b))  # <class 'float'>
    print(type(c))  # <class 'complex'>
    print(type(d))  # <class 'str'>
    print(type(e))  # <class 'bool'>


def fn_3():
    # int
    print(int(12.13))  # 12
    print(int('12'))  # 12
    # print(int('12.13'))
    # ValueError: invalid literal
    # for int() with base 10: '12.13'
    # print(int('hello'))

    # float
    print(float('1314'))  # 1314.0
    print(float('13.14'))  # 13.14
    # print(float('world'))

    # str
    print(str(12))  # '12'
    print(str(1.2))  # '1.2'
    print(str(True))  # 'True'
    print(str([1, 2, 3]))  # '[1, 2, 3]'

    # chr
    print(chr(65))  # A
    print(chr(66))  # B

    # ord
    print(ord('c'))  # 99
    print(ord('d'))  # 100


def excecise_1():
    """华氏温度到摄氏温度 公式为：$C=(F - 32) \div 1.8$。"""
    # tem = float(input('请输入华氏温度: '))
    tem = random.randint(0, 212)
    print(f"华氏温度： { tem }")
    print(f"摄氏温度： { (tem - 32) * 5 / 9 }")


def excecise_2():
    """输入半径计算圆的周长和面积"""
    # r = float(input('请输入圆的半径: '))
    r = random.randint(1, 12)
    print(f"半径： { r }")
    print(f"周长： { math.tau * r }")
    print(f"面积： { math.pi * math.pow(r,2) }")


def excecise_3():
    """输入年份判断是不是闰年"""
    # y = int(input('请输入年份: '))
    y = random.randint(0, 2050)
    print(f"年份： { y }")

    is_leap = False
    if y % 400 == 0:
        if y % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        if y % 4 == 0:
            is_leap = True
        else:
            is_leap = False

    print(f"是否闰年： { '是' if is_leap else '不是' }")


def excecise_3_2():
    y = random.randint(0, 2050)
    print(f"年份： { y }")
    is_leap = False

    if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
        is_leap = True
    else:
        is_leap = False

    print(f"是否闰年： { '是' if is_leap else '不是' }")


def excecise_3_3():
    y = random.randint(0, 2050)
    print(f"年份： { y }")
    print(f"是否闰年： { '是' if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0) else '不是' }")


if __name__ == '__main__':
    fn_1()
    fn_2()
    fn_3()
    excecise_1()
    excecise_2()
    excecise_3()
    excecise_3_2()
    excecise_3_3()
