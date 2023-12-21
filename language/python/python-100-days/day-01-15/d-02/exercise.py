# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-01-18 19:37:30
Description    :
'''
import random
import math


def fahrenheit_to_celsius():
    """_华氏温度转换摄氏温度_
    公式为：$C=(F - 32) \div 1.8$
    """
    # tem = float(input('请输入华氏温度: '))
    tem = random.randint(0, 212)
    print(f"华氏温度： { tem }")
    print(f"摄氏温度： { (tem - 32) * 5 / 9 }")


def calculate_circle_perimeters_areas():
    """_输入半径计算圆的周长和面积_
    """
    # r = float(input('请输入圆的半径: '))
    r = random.randint(1, 12)
    print(f"半径： { r }")
    print(f"周长： { math.tau * r }")
    print(f"面积： { math.pi * math.pow(r,2) }")


def is_leap_year():
    """_判断输入年份是不是闰年_
    """
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


def is_leap_year_2():
    """_判断输入年份是不是闰年_
    """
    y = random.randint(0, 2050)
    print(f"年份： { y }")
    is_leap = False

    if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
        is_leap = True
    else:
        is_leap = False

    print(f"是否闰年： { '是' if is_leap else '不是' }")


def is_leap_year_3():
    """_判断输入年份是不是闰年_
    """
    y = random.randint(0, 2050)
    print(f"年份： { y }")
    print(f"是否闰年： { '是' if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0) else '不是' }")


if __name__ == '__main__':
    fahrenheit_to_celsius()
    calculate_circle_perimeters_areas()
    is_leap_year()
    is_leap_year_2()
    is_leap_year_3()
