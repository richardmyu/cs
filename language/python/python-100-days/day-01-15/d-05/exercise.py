# -*- coding: utf-8 -*-

from tool import is_perfect_n, is_prime


def fn_example():
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


def exercise_1(n=20):
    """生成斐波那契数列的前20个数"""
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n > 2:
        sum = 0
        last_list = exercise_1(n - 1)

        for x in last_list[-2:]:
            sum += x

        return last_list + [sum]


def exercise_2(n=10000):
    """找出 10000 以内的完美数"""
    perfect_n = []

    for x in range(1, n):
        if is_perfect_n(x):
            perfect_n.append(x)

    print(perfect_n)


def exercise_3(n=100):
    """输出 100 以内所有的素数"""
    prime_n = []

    for x in range(1, n):
        if is_prime(x):
            prime_n.append(x)

    print(prime_n)


if __name__ == '__main__':
    print(exercise_1())
    exercise_2()
    exercise_3()
