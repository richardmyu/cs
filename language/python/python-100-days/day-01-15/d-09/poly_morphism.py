# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-02-13 23:12:18
Description    : 该模块提供了在 Python 中定义 抽象基类 (ABC) 的组件
                https://docs.python.org/zh-cn/3/library/abc.html
'''
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]

    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
