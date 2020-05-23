#!/usr/bin/python3
""" unittest for max_integer function module """
import unittest
max_integer = __import__('6-max_integer').max_integer


class max_integer_test(unittest.TestCase):

    def test_positive(self):
        """ """
        self.assertAlmostEqual(max_integer([3, 6, 9, 12]), 12)

    def test_nevative(self):
        """ """
        self.assertEqual(max_integer([-3, -6, -9, -12]), -3)

    def test_list(self):
        """ empty list """
        self.assertEqual(max_integer([]), None)
        """ one digit list """
        self.assertEqual(max_integer([1]), 1)
