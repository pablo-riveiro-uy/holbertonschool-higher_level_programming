#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negatives(self):
        self.assertAlmostEqual(max_integer([-17, -5, -2, -11]), -2)

    def test_one_only_value(self):
        self.assertAlmostEqual(max_integer([5]), 5)

    def test_empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_values_disordered(self):
        self.assertAlmostEqual(max_integer([2, 15.8, 2, 6]), 15.8)


if __name__ == "__main__":
    unittest.main()
