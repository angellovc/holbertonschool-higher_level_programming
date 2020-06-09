#!/usr/bin/python3
import unittest
from models.base import Base

class Base_test(unittest.TestCase):
    
    def test_assignement(self):
        b1 = Base()
        self.assertTrue(b1.id == 1)

    def test_dd(self):
        b2 = Base()
        self.assertTrue(b2.id == 2)
