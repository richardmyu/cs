# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-02-12 20:57:58
Description    :
'''

class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def print_ino(self):
        for key, value in Person.__dict__.items():
            if key.startswith('_') and not key.startswith('__'):
                print(f'{key}: {value}')


def main():
    person = Person('王大锤', 22)
    person.print_ino()
    person._gender = '男'
    person.print_ino()

    # person._is_gay = True
    # AttributeError: 'Person' object has no attribute '_is_gay'


if __name__ == '__main__':
    main()
