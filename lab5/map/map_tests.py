import unittest
from map import *

class TestCases(unittest.TestCase):
   def test_1(self):
      self.assertAlmostEqual(square_all([1]),[1])
     
   def test_square_all_1(self):
      self.assertAlmostEqual(square_all([1,2]),[1,4])

   def test_square_all_2(self):
      self.assertAlmostEqual(square_all([1,2,3,4,5]),[1,4,9,16,25])


   def test_add_n_all_1(self):
      self.assertAlmostEqual(add_n_all(1,[1,2,3,4,5,6,7]),[2,3,4,5,6,7,8])

   def test_add_n_all_2(self):
      self.assertAlmostEqual(add_n_all(100,[1,5,10,15,20,25,1.2]),[101,105,110,115,120,125,101.2])   

   def test_even_odd_all_1(self):
      self.assertAlmostEqual(even_or_odd_all([1,0]),[False,True])
   
   def test_even_odd_all_2(self):
      self.assertAlmostEqual(even_or_odd_all([2,4,6,8,0.1,1,3,5,7,10]),[True,True,True,True,False,False,False,False,False,True])
if __name__ == '__main__':
   unittest.main()

