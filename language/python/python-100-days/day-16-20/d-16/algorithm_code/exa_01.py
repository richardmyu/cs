"""
查找 - 顺序查找和二分查找
算法 - 解决问题的方法（步骤）

评价一个算法的好坏主要有两个指标 - 渐近时间复杂度和渐近空间复杂度，
通常一个算法很难做到时间复杂度和空间复杂度都很低（因为时间和空间是不可调和的矛盾）

表示渐近时间复杂度通常使用大O标记
O(c)           - 常量时间复杂度                   - 哈希存储 / 布隆过滤器
O(log_2 n)     - 对数时间复杂度                   - 折半查找
O(n)           - 线性时间复杂度                   - 顺序查找
O(n * log_2 n) - 对数线性时间复杂度                - 高级排序算法（归并排序、快速排序）
O(n ** 2)      - 平方时间复杂度                   - 简单排序算法（冒泡排序、选择排序、插入排序）
O(n ** 3)      - 立方时间复杂度 / 多项式时间复杂度   - Floyd 算法 / 矩阵乘法运算
O(2 ** n)      - 几何级数时间复杂度                - 汉诺塔
O(3 ** n)      - 几何级数时间复杂度 / 指数时间复杂度
O(n!)          - 阶乘时间复杂度                   - 旅行经销商问题 / NP
"""

from math import log2, factorial
from matplotlib import pyplot

import numpy


def seq_search(items: list, elem) -> int:
    """顺序查找"""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


def bin_search(items, elem):
    """二分查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def main():
    """主函数（程序入口）"""
    num_1 = 6
    num_2 = 7
    styles_1 = ['r-.', 'g-*', 'b-o', 'y-x']
    styles_2 = ['c-^', 'm-+', 'k-d']
    legends_1 = ['对数', '线性', '线性对数', '平方']
    legends_2 = ['立方', '几何级数', '阶乘']

    # 横坐标
    x_data_1 = [x for x in range(1, num_1 + 1)]
    x_data_2 = [x for x in range(1, num_2 + 1)]

    # 对数
    y_data1 = [log2(y) for y in range(1, num_1 + 1)]

    # 线性
    y_data2 = [y for y in range(1, num_1 + 1)]

    # 线性对数
    y_data3 = [y * log2(y) for y in range(1, num_1 + 1)]

    # 平方
    y_data4 = [y**2 for y in range(1, num_1 + 1)]

    # 立方
    y_data5 = [y**3 for y in range(1, num_2 + 1)]

    # 几何级数
    y_data6 = [3**y for y in range(1, num_2 + 1)]

    # 阶乘
    y_data7 = [factorial(y) for y in range(1, num_2 + 1)]

    y_datas_1 = [y_data1, y_data2, y_data3, y_data4]
    y_datas_2 = [y_data5, y_data6, y_data7]

    pyplot.rcParams['font.sans-serif'] = ['SimHei']

    # plot 1
    pyplot.subplot(1, 2, 1)
    for index, y_data in enumerate(y_datas_1):
        pyplot.plot(x_data_1, y_data, styles_1[index])
    pyplot.legend(legends_1)
    pyplot.xticks(numpy.arange(1, num_1 + 1, step=1))
    pyplot.yticks(numpy.arange(0, (num_1 + 1) * 10, step=10))

    # plot 2
    pyplot.subplot(1, 2, 2)
    for index, y_data in enumerate(y_datas_2):
        pyplot.plot(x_data_2, y_data, styles_2[index])
    pyplot.legend(legends_2)
    pyplot.xticks(numpy.arange(1, num_2 + 1, step=1))
    pyplot.yticks(numpy.arange(0, (num_2 + 1) * 700, step=700))

    pyplot.show()


if __name__ == '__main__':
    main()
