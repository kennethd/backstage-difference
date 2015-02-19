
import unittest

from differencesvc import difference

class TestDifference(unittest.TestCase):

    def test_sum_squares(self):
        self.assertEqual(difference.sum_squares(10), 385)

    def test_square_sums(self):
        self.assertEqual(difference.square_sums(10), 3025)

    def test_difference(self):
        self.assertEqual(difference.difference(10), 2640)

