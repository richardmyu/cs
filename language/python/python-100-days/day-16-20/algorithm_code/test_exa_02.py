from unittest import TestCase
from exa_02 import select_sort,merge

class TestExa02(TestCase):
    def setUp(self):
        self.data1 = [35, 97, 12, 68, 55, 73, 81, 40]
        self.items1 = [12, 35, 68, 97]
        self.items2 = [40, 55, 73, 81]

    def test_merge(self):
        items=merge(self.items1,self.items2)
        for i in range(len(items)-1):
            self.assertLessEqual(items[i],items[i+1])

    def test_select_sort(self):
        items=select_sort(self.data1)
        for i in range(len(items)-1):
            self.assertLessEqual(items[i],items[i+1])