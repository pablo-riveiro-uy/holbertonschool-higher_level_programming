#!/usr/bin/python3
import unittest

import ../6-max_integer

class MyTests(unittest.TestCase):
    def testIsList(self):
        self.assertIsInstance(self.list, list)