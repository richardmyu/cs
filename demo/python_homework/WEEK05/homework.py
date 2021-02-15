# -*- coding: utf-8 -*-

import re


# 1.太长了，没兴趣

# 2.python_homework 合法标识符判断
def is_good_name(n):
    # 没有非法字符
    if re.search(r'[^a-zA-Z0-9_]', n):
        return False
    else:
        # 非数字开头
        if re.match(r'[0-9]', n):
            return False
        else:
            return True


print(is_good_name('abc'))
print(is_good_name('_def'))
print(is_good_name('21gh'))
