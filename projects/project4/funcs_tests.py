import unittest
from funcs import *

class TestCases(unittest.TestCase):
   def test_column_search_1(self):
      self.assertAlmostEqual(check_column(['WCALPOLYXU', 'ABPDOEGCVU', 'QMXENDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU'],"CALPOLY"),0)


   def test_row_search_1(self):
      self.assertEqual(check_row(['WAQHGTTWEE', 'CBMIVQQELS', 'APXWKWIIIL', 'LDELFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ'],"POND"),4)


   def test_row_search_2(self):
       self.assertEqual(check_row(["HELLO","GOODBYE"],"HELL"),0)

if __name__ == '__main__':
   unittest.main()
