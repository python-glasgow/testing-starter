"""
A quick starter file for writing tests with Python. This will work on Python
2.7 and 3.3+

2.7 Docs: https://docs.python.org/2/library/unittest.html
3.6 Docs: https://docs.python.org/3.6/library/unittest.html
"""

import unittest


def my_function():
    raise Exception("Failed")


class MyTests(unittest.TestCase):

    def test_equals(self):
        self.assertEqual("Hello", "Hello")

    def test_not_equals(self):
        self.assertNotEqual("Hello", "Hello")

    def test_1_in_range(self):
        self.assertIn(1, range(5))

    def test_exception_is_raised(self):
        with self.assertRaises(Exception):
            my_function()


if __name__ == '__main__':
    unittest.main()
