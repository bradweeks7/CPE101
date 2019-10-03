import unittest
from logic import *

class TestCases(unittest.TestCase):
    def test_function_names(self):
        is_even(0) 
        in_an_interval(0)

    def test_is_even_1(self):
       self.assertTrue(is_even(2))

    def test_in_an_interval_1(self):
       self.assertTrue(in_an_interval(2))
       self.assertFalse(in_an_interval(9))
       
    def test_in_an_interval_2(self):
       self.assertFalse(in_an_interval(47))
       self.assertFalse(in_an_interval(92))

    def test_in_an_interval_3(self):
       self.assertFalse(in_an_interval(12))
       self.assertTrue(in_an_interval(19))

    def test_in_an_interval_4(self):
       self.assertTrue(in_an_interval(101))
       self.assertTrue(in_an_interval(103))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

