# -*- coding: utf-8 -*-

import unittest

from prime import check_prime
from prime_factor import decomposition_prime_factor


class MyTestCasel(unittest.TestCase):
    def test_check_prime(self):
        self.assertEqual(check_prime(1), False)
        self.assertEqual(check_prime(2), True)
        self.assertEqual(check_prime(4), False)
        self.assertEqual(check_prime(7), True)


if __name__ == '__main__':
    unittest.main()
