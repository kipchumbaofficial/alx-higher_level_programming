#!/usr/bin/python3
"""6-max_integer test module
Uses unittest
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests max_integer using unittest module"""

    """setup"""
    def setUp(self):
        self.test_list = [1, 5, 4, 2, 9, 3]
        self.empty_list = []
        self.none_error = "object of type 'NoneType' has no len()"
        self.max_beginning = [5, 3, 2, 4]
        self.max_ending = [5, 3, 4, 7, 10]
        self.test_negatives = [-4, -10, -3, -6, -8]
        self.one_negative = [1, 3, 6, -4, 10]
        self.one_element = [10]

    """Test if list is empty"""
    def test_empty(self):
        self.assertIsNone(max_integer(self.empty_list))

    """Test if output is correct"""
    def test_list(self):
        self.assertEqual(max_integer(self.test_list), 9)

    """Test if no argument is passed to function"""
    def test_no_args(self):
        self.assertIsNone(max_integer())

    """Test if None is passed"""
    def test_none(self):
        with self.assertRaises(TypeError) as err:
            c = max_integer(None)
        self.assertEqual(str(err.exception), self.none_error)

    """Test max in the beginning"""
    def test_max_start(self):
        self.assertEqual(max_integer(self.max_beginning), 5)

    def test_max_end(self):
        self.assertEqual(max_integer(self.max_ending), 10)

    def test_negatives(self):
        self.assertEqual(max_integer(self.test_negatives), -3)

    def test_one_negative(self):
        self.assertEqual(max_integer(self.one_negative), 10)

    def test_one_element(self):
        self.assertEqual(max_integer(self.one_element), 10)


if __name__ == '__main__':
    unittest.main()
