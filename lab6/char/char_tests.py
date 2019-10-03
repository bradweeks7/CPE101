import unittest
from char import *

class TestChar(unittest.TestCase):
   def test_lower_1(self):
      self.assertEqual(is_lower_101('A'),False)
   def test_lower_2(self):
      self.assertEqual(is_lower_101('a'),True)
   def test_char_rot_1(self):
      self.assertEqual(char_rot_13('a'),'n')
   def test_char_rot_2(self):
      self.assertEqual(char_rot_13('b'), 'o')
   def test_char_rot_3(self):
      self.assertEqual(char_rot_13('N'),'A')
   def test_char_rot_4(self):
      self.assertEqual(char_rot_13('('),'(')
    


if __name__ == '__main__':
   unittest.main()

