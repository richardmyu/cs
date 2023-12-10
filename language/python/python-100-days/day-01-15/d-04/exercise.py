# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-01-18 21:27:27
Description    :
'''
import random
from tool import is_comprime


def exercise_1():
    '''输入一个正整数判断是不是素数'''
    num = int(input('请输入一个正整数: '))

    if num <= 0 or int(num) != num:
        print('请输入一个正整数')
        return void

    is_prime = True

    for x in range(2, int(num / 2) + 1):
        if num % x == 0:
            is_prime = False
            break

    print(f'{num} 是素数' if (is_prime and num != 1) else f'{num} 不是素数')


def exercise_2():
    '''输入两个正整数，计算它们的最大公约数和最小公倍数。'''
    a = int(input('请输入一个正整数: '))
    b = int(input('请再输入一个正整数: '))
    gcd = 1
    lcm = 1

    if a <= 0 or int(a) != a or b <= 0 or int(b) != b:
        print('请输入正整数')
        return

    if a % b == 0:
        gcd = b
        lcm = a
    elif b % a == 0:
        gcd = a
        lcm = b
        return
    elif is_comprime(a, b):
        lcm = a * b
    else:
        di = 2
        end = int((max(a, b) / 2))

        for x in range(end + 1, 2, -1):
            if a % x == 0 and b % x == 0 and x > di:
                di = x

        gcd = di
        lcm = int(a * b / di)

    print(f'正整数 { a } 和 { b }: ')
    print(f'最大公约数是：{ gcd }')
    print(f'最小公倍数是：{ lcm }')


def exercise_3():
    '''打印如下所示的三角形图案'''
    # print()
    row = int(input('请输入行数: '))

    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()


if __name__ == '__main__':
    exercise_1()
    exercise_2()
    exercise_3()
