import unittest
import math
from src.lab1.calculator import calc


class CalculatorTestCase(unittest.TestCase):

    def test_sum(self):
        """
        Test sum operation.

        Input: two numbers
        Output: sum of the numbers
        """
        self.assertEqual(calc(2, 3, "+"), 5)
        self.assertEqual(calc(-5, 10, "+"), 5)
        self.assertEqual(calc(0, 0, "+"), 0)

    def test_subtraction(self):
        """
        Test subtraction operation.

        Input: two numbers
        Output: difference between the numbers
        """
        self.assertEqual(calc(5, 3, "-"), 2)
        self.assertEqual(calc(10, -5, "-"), 15)
        self.assertEqual(calc(0, 0, "-"), 0)

    def test_multiplication(self):
        """
        Test multiplication operation.

        Input: two numbers
        Output: product of the numbers
        """
        self.assertEqual(calc(2, 3, "*"), 6)
        self.assertEqual(calc(-5, 10, "*"), -50)
        self.assertEqual(calc(0, 5, "*"), 0)

    def test_division(self):
        """
        Test division operation.

        Input: two numbers
        Output: quotient of the numbers
        """
        self.assertEqual(calc(6, 2, "/"), 3)
        self.assertEqual(calc(1, 2, "/"), 0.5)
        self.assertEqual(calc(-10, 5, "/"), -2)
        self.assertEqual(calc(0, 5, "/"), 0)

    def test_division_by_zero(self):
        """
        Test division by zero.

        Input: two numbers where the second number is zero
        Output: error message
        """
        self.assertEqual(calc(6, 0, "/"), None)

    def test_percentage(self):
        """
        Test percentage operation.

        Input: two numbers
        Output: percentage of the second number with respect to the first number
        """
        self.assertEqual(calc(50, 200, "%"), 25)
        self.assertEqual(calc(100, 50, "%"), 200)
        self.assertEqual(calc(0, 100, "%"), 0)

    def test_pow_operator(self):
        """
        Test empty operator.

        Input: two numbers with an empty operator
        Output: product of the numbers
        """
        self.assertEqual(calc(2, 3, "**"), 8)
        self.assertEqual(calc(-5, 10, "**"), (-5)**10)
        self.assertEqual(calc(0, 5, "**"), 0)

    def test_logarithm(self):
        """
        Test logarithm operation.

        Input: two numbers
        Output: logarithm of the first number with base equal to the second number
        """
        self.assertEqual(calc(100, 10, "log"), 2)
        self.assertEqual(calc(16, 2, "log"), 4)
        self.assertEqual(calc(1, 10, "log"), 0)

    def test_invalid_operator(self):
        """
        Test invalid operator.

        Input: two numbers with an invalid operator
        Output: error message
        """
        self.assertEqual(calc(2, 3, "abc"), None)


