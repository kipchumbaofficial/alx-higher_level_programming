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


if __name__ == '__main__':
    unittest.main()
