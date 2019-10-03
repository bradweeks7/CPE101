import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):

   def test_distance_1(self):
      p1 = Point(0,0)
      p2 = Point(3,4)
      self.assertTrue(distance(p1,p2),5)  

   def test_1(self):
      point_list = [Point(1,0),Point(0,1),Point(0,0)]
      distances = [1,1,0]
      self.assertEqual(distance_all(point_list),distances)
      


   def test_first_quadrant_1(self):
      point_list = [Point(1,1),Point(-1,0),Point(8,1),Point(1,-1),Point(-1,-1)]
      self.assertEqual(are_in_first_quadrant(point_list),[Point(1,1),Point(8,1)])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

