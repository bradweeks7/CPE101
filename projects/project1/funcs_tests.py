import unittest 
from funcs import *

class TestCases(unittest.TestCase):
   def test_poundsToKG_1(self):
      self.assertAlmostEqual(poundsToKG(0), 0.0)
      
   def test_getMassObject_1(self):
      self.assertEqual(getMassObject('t'), 0.1)
      
   def test_getVelocityObject_1(self):
      self.assertAlmostEqual(getVelocityObject(0), 0.0)
           
   def test_getVelocitySkater_1(self):
      self.assertAlmostEqual(getVelocitySkater(100, 0, 100), 0.0)     

   def test_getVelocitySkater_2(self):
      self.assertAlmostEqual(getVelocitySkater(300,9.07,7),0.2116333)

   def test_getVelocitySkater_3(self):
      self.assertRaises(ZeroDivisionError,getVelocitySkater, 0, 10, 10)

   def test_poundsToKG_2(self):
      self.assertAlmostEqual(poundsToKG(100), 45.3592)

   def test_getMassObject_2(self):
      self.assertEqual(getMassObject('l'), 9.07)

   def test_getMassObject_3(self):
      self.assertEqual(getMassObject('z'), 0.0)

   def test_getMassObject_4(self):
      self.assertEqual(getMassObject('r'), 3.0)

   def test_getMassObject_5(self):
      self.assertEqual(getMassObject('g'), 5.3)

   def test_getMassObject_6(self):
      self.assertEqual(getMassObject('lightsaber'), 0.0)

   def test_getVelocityObject_2(self):
      self.assertAlmostEqual(getVelocityObject(1), 2.213594362)

if __name__ == '__main__':
   unittest.main()

