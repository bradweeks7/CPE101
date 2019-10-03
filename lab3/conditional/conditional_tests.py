import unittest
from conditional import *

class TestCases(unittest.TestCase):
    def test_function_names(self):
        max_101(0, 0)
        max_of_three(0, 0, 0)
        rental_late_fee(0)

# Run the unit tests.
    
    #max_101 tests

    def test_max_101_1(self):
        self.assertAlmostEqual(max_101(0,3),3)
    def test_max_101_2(self):
        self.assertEqual(max_101(1000,999),1000)
    def test_max_101_3(self):
        self.assertEqual(max_101(20,20),20)

    #max_of_three tests

    def test_max_of_three_1(self):
        self.assertEqual(max_of_three(20.3,30.4,40.5),40.5)

    def test_max_of_three_2(self):
        self.assertEqual(max_of_three(20,20.1,20.11),20.11)

    #rental_late_fee tests

    def test_rental_late_fee_1(self):
        self.assertEqual(rental_late_fee(15),7)

    def test_rental_late_fee_2(self):
        self.assertEqual(rental_late_fee(25),100)    

if __name__ == '__main__':
    unittest.main()

