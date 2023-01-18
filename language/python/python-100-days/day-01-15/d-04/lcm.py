# -*- coding: utf-8 -*-

'''
@Time: 2023/01/18 23:14:17
@Author: yum
@Email: richardminyu@foxmail.com
@File: lcm.py

最小公倍数常见集中方法的实现
--质因数分解法
--公式法
'''


def lcm(a, b):
    """质因数分解法"""
    if a % b == 0:
        return a
    elif b % a == 0:
        return b
    else:
        a_list = []
        b_list = []
        multiple = 1

        # 分解质因数
        for x in range(2, max(a, b)):
            if a % x == 0 and check_prime(x):
                a_list.append(x)

            if b % x == 0 and check_prime(x):
                b_list.append(x)

        # 获得交集
        # a_union_b = list(set(a_list) | set(b_list))
        total_list = a_list + b_list

        print('--', a_list)
        print('--', b_list)
        print('--', total_list)
        for y in total_list:
            multiple *= y

        return multiple


if __name__ == '__main__':
    print(lcm(9, 21))
    print(lcm(9, 27))
    print(lcm(12, 56))
    print(lcm(21, 56))
