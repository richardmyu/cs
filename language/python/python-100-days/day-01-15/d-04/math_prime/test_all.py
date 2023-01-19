# -*- coding: utf-8 -*-

import unittest

from prime import n_is_prime
from prime_factorization import factorise_prime
from gcd import gcd_prime_1, gcd_prime_2


class MyTestCasel(unittest.TestCase):
    def test_n_is_prime(self):
        self.assertEqual(n_is_prime(1), False)
        self.assertEqual(n_is_prime(2), True)
        self.assertEqual(n_is_prime(3), True)
        self.assertEqual(n_is_prime(4), False)
        self.assertEqual(n_is_prime(7), True)
        self.assertEqual(n_is_prime(1234567890), False)

    def test_factorise_prime(self):
        self.assertEqual(factorise_prime(3), [1, 3])
        self.assertEqual(factorise_prime(4), [2, 2])
        self.assertEqual(factorise_prime(6), [2, 3])
        self.assertEqual(factorise_prime(8), [2, 2, 2])
        self.assertEqual(factorise_prime(64), [2, 2, 2, 2, 2, 2])
        self.assertEqual(factorise_prime(100), [2, 2, 5, 5])

    def test_gcd_prime_1(self):
        self.assertEqual(gcd_prime_1(2, 3), 1)
        self.assertEqual(gcd_prime_1(2, 4), 2)
        self.assertEqual(gcd_prime_1(2, 5), 1)
        self.assertEqual(gcd_prime_1(12, 3), 3)
        self.assertEqual(gcd_prime_1(12, 18), 6)
        self.assertEqual(gcd_prime_1(14, 21), 7)
        self.assertEqual(gcd_prime_1(144, 180), 36)

    def test_gcd_prime_2(self):
        print('--')
        # self.assertEqual(gcd_prime_2(2, 3), 1)
        # self.assertEqual(gcd_prime_2(2, 4), 2)
        # self.assertEqual(gcd_prime_2(2, 5), 1)
        # self.assertEqual(gcd_prime_2(12, 3), 3)
        # self.assertEqual(gcd_prime_2(12, 18), 6)
        # self.assertEqual(gcd_prime_2(14, 21), 7)
        # self.assertEqual(gcd_prime_2(144, 180), 36)


if __name__ == '__main__':
    unittest.main()
