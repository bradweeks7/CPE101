import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality_1(self):
      p1 = Point(0,0)
      p2 = Point(0,0)
      self.assertEqual(p1,p2)
       
   def test_equality_2(self):
      p1 = Point()
      p2 = Point()
      self.assertEqual(p1,p2)


   def test_equality_3(self):
      p1 = Point(y=1)
      p2 = Point(y=1)
      self.assertEqual(p1,p2)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

