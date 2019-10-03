import unittest
from funcs import f
from funcs import g
from funcs import hypotenuse
from funcs import is_positive

class TestCases(unittest.TestCase):
   def test_f_1(self):
    self.assertEqual(f(0),0)
        
   def test_f_2(self):
    self.assertEqual(f(2),32)

   def test_g_1(self):
    self.assertRaises(ZeroDivisionError,g, 0, 3)
      
   def test_g_2(self):
    self.assertEqual(g(3,3),2)     

   def test_hypotenuse_1(self):
    self.assertEqual(hypotenuse(3,4),5)

   def test_hypotensue_2(self):
    self.assertEqual(hypotenuse(-4,3),5)

   def test_is_positive_1(self):
    self.assertTrue(is_positive(1),True)

   def test_is_positive_2(self):
    self.assertFalse(is_positive(-1),False)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

