import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point_1(self):
      p = Point(1,2)
      self.assertEqual(p.x,1)
      self.assertEqual(p.y,2)

   def test_point_2(self):
      p = Point()
      self.assertEqual(p.x,0)
      self.assertEqual(p.y,0)
      

   def test_circle_1(self):
      cir = Circle(Point(1,1),2)
      self.assertEqual(cir.center.y, 1)
      self.assertEqual(cir.center.x,1)
      self.assertEqual(cir.radius,2)

   def test_circle_2(self):
      cir = Circle(Point())
      self.assertEqual(cir.center.y, 0)
      self.assertEqual(cir.center.x,0)
      self.assertEqual(cir.radius,0)

   # Add other testing functions

   def test_distance(self):
      p1 = Point(3,4)
      p2 = Point(0,0)
      self.assertEqual(distance(p1,p2),5)


   def test_overlap_1(self):
      c1 = Circle(Point(0,0),2)
      c2 = Circle(Point(1,1),2)
      self.assertTrue(circles_overlap(c1,c2))

   def test_overlap_2(self):
      c1 = Circle(Point())
      c2 = Circle(Point(10,10),100)
      self.assertTrue(circles_overlap(c1,c2))
if __name__ == '__main__':
   unittest.main()

