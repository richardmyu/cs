# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-02-11 21:28:11
Description    :
'''

class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    main()
