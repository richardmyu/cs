# -*- coding: utf-8 -*-

'''
@Time: 2023/01/15 22:15:05
@Author: yum
@Email: richardminyu@foxmail.com
@File: d-01.py

test start!
'''

import sys
import turtle


print("Hello World!")
print(sys.version_info)
print(sys.version)

############
# exercise #
############

# 1.import this
"""
Beautiful is better than ugly.
优美优于丑陋。

Explicit is better than implicit.
明了优于隐晦。

Simple is better than complex.
简洁优于复杂。

Complex is better than complicated.
复杂优于混乱。

Flat is better than nested.
扁平优于嵌套。

Sparse is better than dense.
间隔优于紧凑。

Readability counts.
可读性很重要。

Special cases aren't special enough to break the rules.
特殊情况也不应该违反这些规则。

Although practicality beats purity.
但现实往往并不那么完美。

Errors should never pass silently.
异常不应该被静默处理。

Unless explicitly silenced.
除非你希望如此。

In the face of ambiguity, refuse the temptation to guess.
遇到模棱两可的地方，不要胡乱猜测。

There should be one-- and preferably only one --obvious way to do it.
肯定有一种通常也是唯一一种最佳的解决方案。


Although that way may not be obvious at first unless you're Dutch.
虽然这种方案并不是显而易见的，因为你不是那个荷兰人[这里指的是Python之父Guido]。

Now is better than never.
现在开始做比不做好。

Although never is often better than *right* now.
不做比盲目去做好 [极限编程中的 YAGNI 原则]。

If the implementation is hard to explain, it's a bad idea.
如果一个实现方案难于理解，它就不是一个好的方案。

If the implementation is easy to explain, it may be a good idea.
如果一个实现方案易于理解，它很有可能是一个好的方案。

Namespaces are one honking great idea -- let's do more of those!
命名空间非常有用，我们应当多加利用！

---

1.[Zen of Python（Python之禅）的最佳翻译](https://zhuanlan.zhihu.com/p/111843067)
2.[蛇宗三字经（The Zen of Python）](https://note.qidong.name/2018/01/the-zen-of-python/)
"""

# 2.学习使用turtle在屏幕上绘制图形

turtle.pensize(4)
turtle.pencolor('red')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()
