import unittest
from city_functions import get_format_city


class CityTestCase(unittest.TestCase):
    def test_format__city(self):
        format_city = get_format_city('santiago', 'chile')
        self.assertEqual(format_city, 'Santiago,Chile')


unittest.main()
