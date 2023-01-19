# -*- coding: utf-8 -*-

import unittest

from prime import n_is_prime
from prime_factorization import factorise_prime


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


if __name__ == '__main__':
    unittest.main()
