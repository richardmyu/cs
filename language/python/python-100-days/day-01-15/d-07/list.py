# -*- coding: utf-8 -*-
def fn_1():
    list1 = [1, 3, 5, 7, 100]

    print(list1)  # [1, 3, 5, 7, 100]

    # 乘号表示列表元素的重复
    list2 = ['hello'] * 3
    print(list2)  # ['hello', 'hello', 'hello']

    # 计算列表长度(元素个数)
    print(len(list1))  # 5

    # 下标(索引)运算
    print(list1[0])  # 1
    print(list1[4])  # 100
    # print(list1[5])
    # # IndexError: list index out of range
    print(list1[-1])  # 100
    print(list1[-3])  # 5
    list1[2] = 300
    print(list1)  # [1, 3, 300, 7, 100]

    # case 1 通过 for 循环遍历列表元素
    for elem in list1:
        print('--in--', elem)

    # case 2 通过循环用下标遍历列表元素
    for index in range(len(list1)):
        print('--range--', list1[index])

    # case 3 通过 enumerate 函数处理列表之后
    # 再遍历可以同时获得元素索引和值
    for index, elem in enumerate(list1):
        print('--enumerate--', index, elem)

    # case 4 使用 iter（）迭代器
    for index in iter(list1):
        print('--iter--', index)


def fn_2():
    list1 = [1, 3, 5, 7, 100]

    # 添加元素
    list1.append(200)
    list1.insert(1, 400)

    # 合并两个列表
    # list1.extend([1000, 2000])
    list1 += [1000, 2000]
    print(list1)
    # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
    print(len(list1))  # 9

    # 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
    if 3 in list1:
        list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    print(list1)
    # [1, 400, 5, 7, 100, 200, 1000, 2000]

    # 从指定的位置删除元素
    list1.pop(0)
    list1.pop(len(list1) - 1)
    print(list1)  # [400, 5, 7, 100, 200, 1000]

    # 清空列表元素
    list1.clear()
    print(list1)  # []


def fn_3():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)  # apple strawberry waxberry

    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)
    # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    fruits4 = fruits[-3:-1]
    print(fruits4)  # ['pitaya', 'pear']

    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)
    # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']


if __name__ == '__main__':
    fn_1()
    fn_2()
    fn_3()