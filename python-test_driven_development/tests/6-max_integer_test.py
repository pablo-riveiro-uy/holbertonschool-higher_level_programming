#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
    def test_value(self):
        self.assertRaises(TypeError, max_integer, "hola")
    def test_negatives(self):
        self.assertAlmostEqual(max_integer([-15, -7, -2, -9]), -2)
    def test_one_only_value(self):
        self.assertAlmostEqual(max_integer([7]), 7)
    def test_empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)
    
if __name__ == "__main__":
    unittest.main()