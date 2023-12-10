# !/usr/bin/env python
# coding= utf-8
'''
Author         : yum <richardminyu@foxmail.com>
Date           : 2023-02-10 21:54:47
LastEditors    : yum <richardminyu@foxmail.com>
LastEditTime   : 2023-12-10 20:03:42
Description    : 使用重新采样和替换来估计一个样本的均值的置信区间

statistical bootstrapping 的示例 https://en.wikipedia.org/wiki/Bootstrapping_(statistics)
'''
from statistics import fmean as mean
from random import choices

data = [41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]
means = sorted(mean(choices(data, k=len(data))) for i in range(100))

print(
    f'The sample mean of {mean(data):.1f} has a 90% confidence '
    f'interval from {means[5]:.1f} to {means[94]:.1f}'
)
