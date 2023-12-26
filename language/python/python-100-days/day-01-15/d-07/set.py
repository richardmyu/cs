# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-01-23 15:36:13
Description    :
'''

def handler_set():
    # 创建集合的字面量语法
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))

    # 创建集合的构造器语法(面向对象部分会进行详细讲解)
    set2 = set(range(1, 10))
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set2, set3)

    # 创建集合的推导式语法(推导式也可以用于推导集合)
    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
    print(set4)

    set5 = {num for num in range(1, 100) if num % 2 == 0 and num % 3 == 0}
    print(set5)


def handler_set_2():
    set1 = {1, 2, 3, 3, 3, 2}
    set2 = set(range(1, 10))
    set3 = set((1, 2, 3, 3, 2, 1))
    print('--set1 before--', set1)
    print('--set2 before--', set2)
    print('--set3 before--', set3)

    set1.add(4)
    set1.add(5)
    print('--set1 after--', set1)

    set2.update([11, 12])
    set2.discard(5)

    if 4 in set2:
        set2.remove(4)

    print('--set2 after--', set2)

    print(set3.pop())
    print(set3)
    print('--set3 after--', set3)


def handler_set_3():
    set1 = {1, 2, 3, 7, 8}
    set2 = {1, 2, 4, 6, 8}
    set3 = {2, 3, 4, 7}

    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2)
    # print(set1.intersection(set2))

    print(set1 | set2)
    # print(set1.union(set2))

    print(set1 - set2)
    # print(set1.difference(set2))

    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))

    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))

    print(set3 <= set1)
    # print(set3.issubset(set1))

    print(set1 >= set2)
    # print(set1.issuperset(set2))

    print(set1 >= set3)
    # print(set1.issuperset(set3))


if __name__ == '__main__':
    # handler_set()
    # handler_set_2()
    handler_set_3()
