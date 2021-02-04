# -*- coding: utf-8 -*-

import math


# 3.已知三角形三边边长分别为 a,b,c，求夹角 C
def calc_angle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print("输入边长有误")
        return 0
    angle_c = math.acos((math.pow(a, 2) + math.pow(b, 2) -
                         math.pow(c, 2)) / (2 * b * c))
    return round(math.degrees(angle_c), 1)


print(calc_angle(3, 4, 5))  # 90.0
