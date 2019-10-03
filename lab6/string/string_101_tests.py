import unittest
import string 
from string_101 import *

class TestString(unittest.TestCase):
   def test_str_rot_1(self):
      self.assertEqual(str_rot_13('abcdefg'),'nopqrst')
   def test_str_rot_2(self):
      self.assertEqual(str_rot_13('1A2b3C4d'),'1N2o3P4q')
   def test_str_translate_1(self):
      self.assertEqual(str_translate_101('a','a','b'),'b')
   def test_str_translate_2(self):
      self.assertEqual(str_translate_101('a(baarb]','a','b'),'b(bbbrb]')
   def test_str_translate_3(self):
      self.assertEqual(str_translate_101('((()))asdfjkl;[[[]]]','[',']'),'((()))asdfjkl;]]]]]]') 

if __name__ == '__main__':
   unittest.main()

