#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

base = __import__('base').Base

class TestBase(unittest.TestCase):

    def testRectangleClass(self):
        rect = Rectangle()
        self.assertAlmostEqual(rect.__name__ == "Rectangle")




if __name__ == "__main__":
    unittest.main()
