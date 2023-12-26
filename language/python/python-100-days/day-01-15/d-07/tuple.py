# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-01-23 15:29:22
Description    :
'''

def handler_tuple():
    # 定义元组
    t = ('kevin', 'bob', True, 'stuart')
    print(t)

    # 获取元组中的元素
    print(t[0])
    print(t[3])

    # 遍历元组中的值
    for member in t:
        print(member)

    # 重新给元组赋值
    # t[0] = 'king bob'  # TypeError

    # 变量 t 重新引用了新的元组原来的元组将被垃圾回收
    t = (1, 20, 12, 6)
    print(t)

    # 将元组转换成列表
    person = list(t)
    print(person)

    # 列表是可以修改它的元素的
    person[0] = 13
    person[1] = 25
    print(person)

    # 将列表转换成元组
    fruits_list = ['1', '2', '3']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)


if __name__ == '__main__':
    handler_tuple()
