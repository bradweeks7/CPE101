import unittest
from filter import *

class TestCases(unittest.TestCase):

   def test_positive_t_1(self):
      self.assertAlmostEqual(are_positive([-1,10,-30,20,0]),[10,20])
      
   def test_positive_t_2(self):
      self.assertAlmostEqual(are_positive([-1,10,-30,20,0]),[10,20])

   def test_are_greater_than_n_1(self):
      self.assertAlmostEqual(are_greater_than_n([1,2,3,4,5,6,7,8],4), [5,6,7,8])

   def test_are_greater_than_n_2(self):
      self.assertAlmostEqual(are_greater_than_n([-1,-5,-61,2,3,4,5,6,7,8],0), [2,3,4,5,6,7,8]) 

   def test_are_divisible_by_n_1(self):
      self.assertAlmostEqual(are_divisible_by_n([2,3,4,5,100,-2],2), [2,4,100,-2])

   def test_are_divisible_by_n_2(self):
      self.assertAlmostEqual(are_divisible_by_n([2.5,3,33,11,12,99],3), [3,33,12,99])


if __name__ == '__main__':
   unittest.main()

