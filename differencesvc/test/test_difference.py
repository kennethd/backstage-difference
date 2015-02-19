
import unittest

from differencesvc import difference

class TestDifference(unittest.TestCase):

    def test_sum_squares(self):
        self.assertEqual(difference.sum_squares(10), 385)
        # enforces n <= 100
        with self.assertRaises(ValueError) as ctx:
            difference.sum_squares(101)
        self.assertEqual(ctx.exception.message, "101 must be integer <= 100")
        # enforces n is int
        with self.assertRaises(ValueError) as ctx:
            difference.sum_squares('a')
        self.assertEqual(ctx.exception.message, "invalid literal for int() with base 10: 'a'")

    def test_square_sums(self):
        self.assertEqual(difference.square_sums(10), 3025)
        # enforces n <= 100
        with self.assertRaises(ValueError) as ctx:
            difference.square_sums(101)
        self.assertEqual(ctx.exception.message, "101 must be integer <= 100")
        # enforces n is int
        with self.assertRaises(ValueError) as ctx:
            difference.square_sums('a')
        self.assertEqual(ctx.exception.message, "invalid literal for int() with base 10: 'a'")

    def test_difference(self):
        self.assertEqual(difference.difference(10), 2640)
        # enforces n <= 100
        with self.assertRaises(ValueError) as ctx:
            difference.difference(101)
        self.assertEqual(ctx.exception.message, "101 must be integer <= 100")
        # enforces n is int
        with self.assertRaises(ValueError) as ctx:
            difference.difference('a')
        self.assertEqual(ctx.exception.message, "invalid literal for int() with base 10: 'a'")

