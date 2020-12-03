# -*- coding: utf-8 -*-

import math
print(math.pi)
# 1.BMI


def calcBMI(weigh, height):
    diff = weigh/(math.pow(height, 2))
    return round(diff, 2)


# print(calcBMI(80, 1.75))  # 26.12

# 2.将秒数分成 时 分 秒


def formatTime(sec):
    if sec < 0:
        print("输入秒数有误")
        return 0
    res = ''
    h = math.floor(sec/(60*60))
    # h = sec//(60*60)
    m = math.floor((sec - h*60*60) / 60)
    s = sec % 60
    res = str(h)+' '+str(m)+' '+str(s)
    return res


# print(formatTime(30))  # 0 0 30
# print(formatTime(61))  # 0 1 1
# print(formatTime(3670))  # 1 1 10
# print(formatTime(70000))  # 19 26 40

# 3.已知三角形三边边长分别为 a,b,c，求夹角 C


def calcAngle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print("输入边长有误")
        return 0
    angC = math.acos((math.pow(a, 2)+math.pow(b, 2) -
                      math.pow(c, 2))/(2*b*c))
    return round(math.degrees(angC), 1)


print(calcAngle(3, 4, 5)) # 90.0
