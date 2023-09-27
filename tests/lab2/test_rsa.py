import unittest

from src.lab2.rsa import is_prime, gcd, multiplicative_inverse


class RsaTest(unittest.TestCase):
    def test_is_prime(self):
        """
        Tests to see if a number is prime.
        """
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(8))

    def test_gcd(self):
        """
        Euclid's algorithm for determining the greatest common divisor.
        """
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)

    def test_multiplicative_inverse(self):
        """
        Euclid's extended algorithm for finding the multiplicative inverse of two numbers.
        """
        self.assertEqual(multiplicative_inverse(7, 40), 23)
