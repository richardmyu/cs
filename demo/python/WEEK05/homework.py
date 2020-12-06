# -*- coding: utf-8 -*-

# 1.太长了，没兴趣

# 2.python 合法标识符判断

import re


def isGoodName(n):
    # 没有非法字符
    if re.search(r'[^a-zA-Z0-9_]', n):
        return False
    else:
        # 非数字开头
        if re.match(r'[0-9]', n):
            return False
        else:
            return True


print(isGoodName('abc'))
print(isGoodName('_def'))
print(isGoodName('21gh'))

# 3.无聊算法


def letToNum(n):
    if re.match(r'[aA]', n):
        return 1
    elif re.match(r'[bB]', n):
        return 2
    elif re.match(r'[cC]', n):
        return 3
    elif re.match(r'[dD]', n):
        return 4
    elif re.match(r'[eE]', n):
        return 5
    elif re.match(r'[fF]', n):
        return 6
    elif re.match(r'[gG]', n):
        return 7
    elif re.match(r'[hH]', n):
        return 8
    elif re.match(r'[iI]', n):
        return 9
    elif re.match(r'[jJ]', n):
        return 10
    elif re.match(r'[kK]', n):
        return 11
    elif re.match(r'[lL]', n):
        return 12
    elif re.match(r'[mM]', n):
        return 13
    elif re.match(r'[nN]', n):
        return 14
    elif re.match(r'[oO]', n):
        return 15
    elif re.match(r'[pP]', n):
        return 16
    elif re.match(r'[qQ]', n):
        return 17
    elif re.match(r'[rR]', n):
        return 18
    elif re.match(r'[sS]', n):
        return 19
    elif re.match(r'[tT]', n):
        return 20
    elif re.match(r'[uU]', n):
        return 21
    elif re.match(r'[vV]', n):
        return 22
    elif re.match(r'[wW]', n):
        return 23
    elif re.match(r'[xX]', n):
        return 24
    elif re.match(r'[yY]', n):
        return 25
    elif re.match(r'[zZ]', n):
        return 26
    else:
        return 0


def calcSum(n):
    sum = 0
    for l in n:
        sum += letToNum(l)
    return sum


print(calcSum('Colin'))  # 53
print(calcSum('ABC'))  # 6
