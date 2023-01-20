# -*- coding: utf-8 -*-


def fn_1():
    """寻找水仙花数"""
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100

        if num == low**3 + mid**3 + high**3:
            print(num)


def fn_2():
    """正整数的反转"""
    num = int(input('num = '))
    reversed_num = 0

    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10

    print(reversed_num)


def fn_3():
    """百钱百鸡"""
    # 5*x + 1/3*y = 100
    # x + y = 100
    # ==> x < 15
    # 3*x + 1/3*y = 100
    # x + y = 100
    # ==> x < 26
    for x in range(0, 15):
        for y in range(0, 26):
            z = 100 - x - y

            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


if __name__ == '__main__':
    # fn_1()
    # fn_2()
    fn_3()
