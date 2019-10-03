import unittest
from fold import *

class TestCases(unittest.TestCase):
   def test_1_sum(self):
      self.assertEqual(list_sum([0,0,0,0]),0) # Add code here.
   def test_2_sum(self):
      self.assertEqual(list_sum([0,1,2,3,4]),10)
   def test_smallest_index(self):
      self.assertEqual(index_of_smallest([5,10,3,1]),3)
   def test_smallest_index_2(self):
      self.assertEqual(index_of_smallest([-10,5,100]),0)
   def test_smallest_index_e(self):
      self.assertEqual(index_of_smallest([]),-1)
   
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

