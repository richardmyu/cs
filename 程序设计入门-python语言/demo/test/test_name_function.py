# -*- coding: utf-8 -*-

"""
测试流程：
1.引入 unittest 和 待测试函数/方法；

2.创建一个测试类(测试样例)，用以包含一系列针对待测试函数/方法的单元测试，且这个类必须继承自 unittest.TestCase；

3.定义测试函数（以 test_ 开头），函数内部调用待测试函数/方法，并进行断言；

"""
import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    # 以 test_ 开头的函数，都会在测试时自动执行
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


# print(__name__)
if __name__ == '__main__':
    unittest.main()

# unittest.main()
