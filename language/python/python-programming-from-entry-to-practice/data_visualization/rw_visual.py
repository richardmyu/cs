# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import time

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, s=1)
    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors='none',
        s=1,
    )

    # 起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=10)
    # plt.savefig(f'random_walk_{time.time()}.png', bbox_inches='tight')

    # 隐藏坐标
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.savefig(f'rw_visual_{time.time()}.png')
    plt.show()

    keep_running = input('Make another walk?(y/n): ')

    if keep_running == 'n':
        break
