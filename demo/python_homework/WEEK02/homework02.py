# -*- coding: utf-8 -*-

import math


# 2.将秒数分成 时 分 秒
def format_time(sec):
    if sec < 0:
        print("输入秒数有误")
        return 0
    h = math.floor(sec / (60 * 60))
    # h = sec//(60*60)
    m = math.floor((sec - h * 60 * 60) / 60)
    s = sec % 60
    res = str(h) + ' ' + str(m) + ' ' + str(s)
    return res


print(format_time(30))  # 0 0 30
print(format_time(61))  # 0 1 1
print(format_time(3670))  # 1 1 10
print(format_time(70000))  # 19 26 40
