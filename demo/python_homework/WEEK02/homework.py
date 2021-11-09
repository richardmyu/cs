# -*- coding: utf-8 -*-

import math


# 1.BMI
def calc_bmi(weigh, height):
    diff = weigh / (math.pow(height, 2))
    return round(diff, 2)


print(calc_bmi(80, 1.75))  # 26.12
