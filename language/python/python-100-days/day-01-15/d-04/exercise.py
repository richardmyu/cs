# -*- coding: utf-8 -*-

import random
import math


def fn_1():
    """1~100之间的偶数求和"""
    sum = 0
    for x in range(2, 101, 2):
        sum += x
    print(sum)


def fn_2():
    """猜数字游戏"""
    answer = random.randint(1, 100)
    counter = 0

    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了 (๑•̀ㅂ•́)و✧ !')
            break

    print(f'你总共猜了 {counter} 次')

    if counter > 7:
        print('超过了 7 次，下次要努力呀！😄😄😄')


def fn_3():
    """输出乘法口诀表(九九表)"""
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d * %d = %d' % (i, j, i * j), end='\t')
        print()


def exercise_1():
    """输入一个正整数判断是不是素数"""
    num = int(input('请输入一个正整数: '))

    if num <= 0 or int(num) != num:
        print('请输入一个正整数')
        return void

    end = int(math.sqrt(num))
    is_prime = True

    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break

    print(f'{num} 是素数' if (is_prime and num != 1) else f'{num} 不是素数')


def exercise_2():
    """输入两个正整数，计算它们的最大公约数和最小公倍数。"""
    a = int(input('请输入一个正整数: '))
    b = int(input('请再输入一个正整数: '))

    if a <= 0 or int(a) != a or b <= 0 or int(b) != b:
        print('请输入正整数')
        return void


def exercise_3():
    """打印如下所示的三角形图案"""
    print()


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    # fn_3()
    exercise_1()
