#!/usr/bin/python3
""" Rectangle test module """
import unittest
import sys
import pep8
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class Rectangle_test(unittest.TestCase):
    """ Rectangle Test """

    def test_pep8(self):
        """ pep8 test """
        pep8style = pep8.StyleGuide(quiet=True)
        output = pep8style.check_files(['models/square.py'])
        self.assertEqual(output.total_errors, 0)

    def test__init__normally(self):
        """ Constructor test normal conditions """
        s = Square(3, 0, 0, 1)
        self.assertTrue(s.id == 1)  # inheritance from Base
        self.assertTrue(s.size == 3)
        self.assertTrue(s.x == 0)
        self.assertTrue(s.y == 0)

    def test__init__arguments_position(self):
        """ Constructor test argument positions """
        with self.assertRaises(TypeError) as error:
            Square()  # zero arguments
        self.assertTrue(str(error.exception) == "\
__init__() missing 1 required positional argument: 'size'")
        s = Square(1)  # one parameter
        self.assertTrue(s.width == 1)
        self.assertTrue(s.height == 1)
        s = Square(2, 2)  # two paramenters: size and x
        self.assertTrue(s.x == 2)
        s = Square(2, 2, 2)  # three paramenters: size, x and y
        self.assertTrue(s.y == 2)

    def test__init__no_allowed_values(self):
        """ Constructor negative numbers and zero """
        with self.assertRaises(TypeError) as error:
            Square("string")  # string size"
        self.assertTrue(str(error.exception) == "width must be an integer")
        with self.assertRaises(TypeError) as error:
            Square([1])  # list size"
        self.assertTrue(str(error.exception) == "width must be an integer")
        with self.assertRaises(TypeError) as error:
            Square(0.0)  # float size"
        self.assertTrue(str(error.exception) == "width must be an integer")
        with self.assertRaises(TypeError) as error:
            Square((2,))  # tuple size"
        self.assertTrue(str(error.exception) == "width must be an integer")

        with self.assertRaises(TypeError) as error:
            Square(10, "string")  # string x"
        self.assertTrue(str(error.exception) == "x must be an integer")
        with self.assertRaises(TypeError) as error:
            Square(10, 10, "string")  # string y"
        self.assertTrue(str(error.exception) == "y must be an integer")
        with self.assertRaises(TypeError) as error:
            Square(1, [1])  # list x"
        self.assertTrue(str(error.exception) == "x must be an integer")
        with self.assertRaises(TypeError) as error:
            Square(1, 1, [1])  # list y"
        self.assertTrue(str(error.exception) == "y must be an integer")
        with self.assertRaises(TypeError) as error:
            Square(1, 0.0)  # float x"
        self.assertTrue(str(error.exception) == "x must be an integer")
        with self.assertRaises(TypeError) as error:
            Square(1, 1, 0.0)  # float y"
        self.assertTrue(str(error.exception) == "y must be an integer")
        with self.assertRaises(TypeError) as error:
            Square(1, (2,))  # tuple X"
        self.assertTrue(str(error.exception) == "x must be an integer")
        with self.assertRaises(TypeError) as error:
            Square(1, 1, (2,))  # tuple y"
        self.assertTrue(str(error.exception) == "y must be an integer")

    def test__init__negative_numbers(self):
        """ Constructor negative numbers and zero """
        with self.assertRaises(ValueError) as error:
            Square(0)  # zero size"
        self.assertTrue(str(error.exception) == "width must be > 0")
        with self.assertRaises(ValueError) as error:
            Square(-10)  # negative size"
        self.assertTrue(str(error.exception) == "width must be > 0")
        s = Square(1, 0, 0)  # zero x, y
        self.assertTrue(s.x == 0)
        self.assertTrue(s.y == 0)
        with self.assertRaises(ValueError) as error:
            Square(10, -1)  # negative x"
        self.assertTrue(str(error.exception) == "x must be >= 0")
        with self.assertRaises(ValueError) as error:
            Square(10, 10, -1)  # negative x"
        self.assertTrue(str(error.exception) == "y must be >= 0")

    def test__init__instances_subclases(self):
        """ check instanciation """
        s = Square(1, 1)
        self.assertTrue(isinstance(s, Square))  # Rectangle instance check
        self.assertTrue(isinstance(s, Square))  # Base instanciation check
        self.assertTrue(issubclass(Square, Base))  # Base subclass

    def test_area(self):
        """ check area method """
        s = Square(2, 4, 9)
        self.assertEqual(s.area(), 4)
        s = Square(2)
        self.assertEqual(s.area(), 4)
        s = Square(1, 40, 10, 1)
        self.assertEqual(s.area(), 1)

    def test_display(self):
        """ check the stdout of display """
        output = StringIO()
        sys.stdout = output
        s1 = Square(4)
        s1.display()
        # widht and height tests #
        self.assertEqual(output.getvalue(), "####\n####\n####\n####\n")
        output = StringIO()
        sys.stdout = output
        s1 = Square(1)
        s1.display()
        self.assertEqual(output.getvalue(), "#\n")
        output = StringIO()
        sys.stdout = output
        s1 = Square(1, 2)
        s1.display()
        self.assertEqual(output.getvalue(), "  #\n")
        # axis tests #
        output = StringIO()
        sys.stdout = output
        s1 = Square(1, 2, 2)
        s1.display()
        self.assertEqual(output.getvalue(), "\n\n  #\n")
        output = StringIO()
        sys.stdout = output
        s1 = Square(3, 2, 1, 1)
        s1.display()
        self.assertEqual(output.getvalue(), "\n  ###\n  ###\n  ###\n")
        sys.stdout = sys.__stdout__

    def test__str__(self):
        """ test to __str__ method """
        s1 = Square(6, 2, 1, 12)
        self.assertEqual(s1.__str__(),  "[Square] (12) 2/1 - 6")
        s1.size = 10
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 10")


if __name__ == "__main__":
    unittest.main()
