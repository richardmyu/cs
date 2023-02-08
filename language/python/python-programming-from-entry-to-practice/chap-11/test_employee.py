import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee('bob', 'potter', 100000)

    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.annual_salary, 105000)

    def test_give_custom_raise(self):
        self.emp.give_raise(50000)
        self.assertEqual(self.emp.annual_salary, 150000)


unittest.main()
