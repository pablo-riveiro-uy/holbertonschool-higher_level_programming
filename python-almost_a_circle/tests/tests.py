#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def testRectangleClass(self):
        base1 = Base()
        self.assertAlmostEqual(base1.id, 1)
        base2 = Base()
        self.assertAlmostEqual(base2.id, 2)
        base3 = Base(12)
        self.assertAlmostEqual(base3.id, 12)
        base4 = Base(-6)
        self.assertAlmostEqual(base4.id, -6)

    def test_save_to_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertAlmostEqual(file.read(), "[]")

    def test_to_json_string(self):
        self.assertAlmostEqual(Base.to_json_string(None), "[]")
        self.assertAlmostEqual(Base.to_json_string([{'id': 1}]),
                               '[{"id": 1}]')
        self.assertAlmostEqual(Base.to_json_string([]), "[]")

    def test_to_dictionary_functionn(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertAlmostEqual(r1 is r2, False)
        self.assertAlmostEqual(r1 == r2, False)


if __name__ == "__main__":
    unittest.main()
