# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-02-11 21:24:55
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

    # AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()

    # AttributeError: 'Test' object has no attribute '__foo'
    print(test.__foo)


if __name__ == '__main__':
    main()
