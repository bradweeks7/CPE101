import unittest
from groups import *

class TestCases(unittest.TestCase):

   def test_groups_of_three_0(self):
      self.assertEqual(groups_of_3([1,2,3,4,5,6,7,8,9]), [[1,2,3],[4,5,6],[7,8,9]])

   def test_groups_of_three_3(self):
      self.assertEqual(groups_of_3([1,2,3,4,5,6,7]),[[1,2,3],[4,5,6],[7]])

   def test_groups_of_three_1(self):
      self.assertEqual(groups_of_3([1,2,3,4,5,6,7,8]),[[1,2,3],[4,5,6],[7,8]])

   def test_groups_of_three_2(self):
      self.assertEqual(groups_of_3([]),[])


if __name__ == '__main__':
   unittest.main()
