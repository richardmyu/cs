import unittest
from prime import is_prime
from prime_factorization import factorise_prime
from comprime import is_comprime
from gcd import gcd_prime_1, gcd_prime_2, gcd_euclidean, gcd_reduce, gcd_division
from lcm import lcm_prime, lcm_formula, lcm_division


class MyTestCasel(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(1234567890), False)

    def test_factorise_prime(self):
        self.assertEqual(factorise_prime(3), [1, 3])
        self.assertEqual(factorise_prime(4), [2, 2])
        self.assertEqual(factorise_prime(6), [2, 3])
        self.assertEqual(factorise_prime(8), [2, 2, 2])
        self.assertEqual(factorise_prime(64), [2, 2, 2, 2, 2, 2])
        self.assertEqual(factorise_prime(100), [2, 2, 5, 5])

    def test_is_comprime(self):
        self.assertEqual(is_comprime(1, 1), True)
        self.assertEqual(is_comprime(2, 3), True)
        self.assertEqual(is_comprime(2, 4), False)
        self.assertEqual(is_comprime(2, 5), True)
        self.assertEqual(is_comprime(12, 3), False)
        self.assertEqual(is_comprime(12, 18), False)
        self.assertEqual(is_comprime(14, 25), True)
        self.assertEqual(is_comprime(121, 180), True)

    def test_gcd_prime_1(self):
        self.assertEqual(gcd_prime_1(2, 3), 1)
        self.assertEqual(gcd_prime_1(2, 4), 2)
        self.assertEqual(gcd_prime_1(2, 5), 1)
        self.assertEqual(gcd_prime_1(12, 3), 3)
        self.assertEqual(gcd_prime_1(12, 18), 6)
        self.assertEqual(gcd_prime_1(14, 21), 7)
        self.assertEqual(gcd_prime_1(144, 180), 36)

    def test_gcd_prime_2(self):
        self.assertEqual(gcd_prime_2(2, 3), 1)
        self.assertEqual(gcd_prime_2(2, 4), 2)
        self.assertEqual(gcd_prime_2(2, 5), 1)
        self.assertEqual(gcd_prime_2(12, 3), 3)
        self.assertEqual(gcd_prime_2(12, 18), 6)
        self.assertEqual(gcd_prime_2(14, 21), 7)
        self.assertEqual(gcd_prime_2(144, 180), 36)

    def test_gcd_euclidean(self):
        self.assertEqual(gcd_euclidean(2, 3), 1)
        self.assertEqual(gcd_euclidean(2, 4), 2)
        self.assertEqual(gcd_euclidean(2, 5), 1)
        self.assertEqual(gcd_euclidean(12, 3), 3)
        self.assertEqual(gcd_euclidean(12, 18), 6)
        self.assertEqual(gcd_euclidean(14, 21), 7)
        self.assertEqual(gcd_euclidean(144, 180), 36)

    def test_gcd_reduce(self):
        self.assertEqual(gcd_reduce(2, 3), 1)
        self.assertEqual(gcd_reduce(2, 4), 2)
        self.assertEqual(gcd_reduce(2, 5), 1)
        self.assertEqual(gcd_reduce(12, 3), 3)
        self.assertEqual(gcd_reduce(12, 18), 6)
        self.assertEqual(gcd_reduce(14, 21), 7)
        self.assertEqual(gcd_reduce(144, 180), 36)

    def test_gcd_division(self):
        self.assertEqual(gcd_division(2, 3), 1)
        self.assertEqual(gcd_division(2, 4), 2)
        self.assertEqual(gcd_division(2, 5), 1)
        self.assertEqual(gcd_division(12, 3), 3)
        self.assertEqual(gcd_division(12, 18), 6)
        self.assertEqual(gcd_division(14, 21), 7)
        self.assertEqual(gcd_division(144, 180), 36)

    def test_lcm_prime(self):
        self.assertEqual(lcm_prime(2, 3), 6)
        self.assertEqual(lcm_prime(2, 4), 4)
        self.assertEqual(lcm_prime(2, 5), 10)
        self.assertEqual(lcm_prime(12, 3), 12)
        self.assertEqual(lcm_prime(12, 18), 36)
        self.assertEqual(lcm_prime(14, 21), 42)
        self.assertEqual(lcm_prime(144, 180), 720)

    def test_lcm_formula(self):
        self.assertEqual(lcm_formula(2, 3), 6)
        self.assertEqual(lcm_formula(2, 4), 4)
        self.assertEqual(lcm_formula(2, 5), 10)
        self.assertEqual(lcm_formula(12, 3), 12)
        self.assertEqual(lcm_formula(12, 18), 36)
        self.assertEqual(lcm_formula(14, 21), 42)
        self.assertEqual(lcm_formula(144, 180), 720)

    def test_lcm_division(self):
        self.assertEqual(lcm_division(2, 3), 6)
        self.assertEqual(lcm_division(2, 4), 4)
        self.assertEqual(lcm_division(2, 5), 10)
        self.assertEqual(lcm_division(12, 3), 12)
        self.assertEqual(lcm_division(12, 18), 36)
        self.assertEqual(lcm_division(14, 21), 42)
        self.assertEqual(lcm_division(144, 180), 720)


if __name__ == '__main__':
    unittest.main()
