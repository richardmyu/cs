# -*- coding: utf-8 -*-

import unittest
from city_full_function import get_format_city


class CityTestCase(unittest.TestCase):
    def test_format__city(self):
        format_city = get_format_city('santiago', 'chile', 5000000)
        self.assertEqual(format_city, 'Santiago,Chile - population 5000000')


unittest.main()
