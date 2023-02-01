# -*- coding: utf-8 -*-

import os
import sys
import time
import random


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


def exercise_1():
    """在屏幕上显示跑马灯文字"""
    content = "hello world "

    while True:
        # 清屏
        os.system('cls')  # os.system('clear')
        print(content)

        time.sleep(0.2)
        content = content[1:] + content[0]


def exercise_2(l=8):
    """产生指定长度的验证码，验证码由大小写字母和数字构成"""
    chars_num = "0123456789"
    chars_str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    char_list = []

    for _ in range(int(l / 2)):
        i = random.randint(0, len(chars_num) - 1)
        char_list.append(chars_num[i : i + 1])

    for _ in range(int(l / 2)):
        i = random.randint(0, len(chars_str) - 1)
        char_list.append(chars_str[i : i + 1])

    random.shuffle(char_list)

    for x in char_list:
        code += str(x)

    return code


def exercise_3(filename):
    """返回给定文件名的后缀名"""
    index = filename.rfind('.')

    if index != -1:
        return filename[(index + 1) :]
    else:
        return 'none'


def exercise_4(l):
    """返回传入的列表中最大和第二大的元素的值"""
    new_l = l[:]
    max_l = max(new_l)

    count = new_l.count(max_l)

    if count >= 1:
        # 去重
        for _ in range(count):
            new_l.remove(max_l)

    sub_max_l = max(new_l)

    return max_l, sub_max_l


def exercise_4_2(l):
    """返回传入的列表中最大和第二大的元素的值"""
    new_l = l[:]
    new_l = list(set(new_l))
    max_l = max(new_l)
    new_l.remove(max_l)
    sub_max_l = max(new_l)

    return max_l, sub_max_l


def is_leap_year(y):
    """是否是闰年"""
    return y % 100 != 0 and y % 4 == 0 or y % 400 == 0


def exercise_5(y, m, d):
    """计算指定的年月日是这一年的第几天"""
    is_leap = is_leap_year(y)
    total_day = d
    months_list = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    ]

    if is_leap:
        for x in range(m - 1):
            total_day += months_list[1][x]
    else:
        for x in range(m - 1):
            total_day += months_list[0][x]

    return total_day


def exercise_6_1(n=5):
    """打印杨辉三角"""
    L = [1]
    count = 0

    while count < n:
        count += 1
        yield L
        L = [sum(i) for i in zip([0] + L, L + [0])]


def exercise_6_2(n=5):
    """打印杨辉三角"""
    ret = [1]
    count = 0
    while count < n:
        count += 1
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]


def exercise_6_3(n=5):
    """打印杨辉三角"""
    LL = [[1]]
    for i in range(1, n):
        LL.append(
            [
                (0 if j == 0 else LL[i - 1][j - 1])
                + (0 if j == len(LL[i - 1]) else LL[i - 1][j])
                for j in range(i + 1)
            ]
        )
    return LL


if __name__ == '__main__':
    generator_expression()
    generator_function()

    for val in generator_yield(20):
        print(val)

    # exercise_1()

    print(exercise_2())
    print(exercise_3('list.py'))
    print(exercise_3('list.py.'))
    print(exercise_3('.editorconfig'))
    print(exercise_4([1, 2, 3, 4]))
    print(exercise_4([1, 2, 3, 4, 5, 2, 5]))
    print(exercise_4_2([1, 2, 3, 4]))
    print(exercise_4_2([1, 2, 3, 4, 5, 2, 5]))
    print(exercise_5(1980, 11, 28))  # 333
    print(exercise_5(1981, 12, 31))  # 365
    print(exercise_5(2018, 1, 1))  # 1
    print(exercise_5(2016, 3, 1))  # 61

    for x in exercise_6_1(1):
        print(x)
    for x in exercise_6_1(2):
        print(x)
    for x in exercise_6_1(3):
        print(x)
    for x in exercise_6_1(4):
        print(x)
    for x in exercise_6_1(5):
        print(x)
    for x in exercise_6_1(6):
        print(x)
    for x in exercise_6_1(7):
        print(x)

    for x in exercise_6_2(1):
        print(x)
    for x in exercise_6_2(2):
        print(x)
    for x in exercise_6_2(3):
        print(x)
    for x in exercise_6_2(4):
        print(x)
    for x in exercise_6_2(5):
        print(x)
    for x in exercise_6_2(6):
        print(x)
    for x in exercise_6_2(7):
        print(x)

    print(exercise_6_3(1))
    print(exercise_6_3(2))
    print(exercise_6_3(3))
    print(exercise_6_3(4))
    print(exercise_6_3(5))
    print(exercise_6_3(6))
    print(exercise_6_3(7))
