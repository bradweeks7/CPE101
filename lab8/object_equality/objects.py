from utility import *


class Point:
   '''
   x - int
   y - int
   '''
   def __init__(self,x=0,y=0):
      self.x = x
      self.y = y
   
   def __eq__(self,other):
      return epsilon_equal(self.x,other.x) and epsilon_equal(self.y,other.y);

class Circle:
   '''
   center - Point(int,int)
   radius - float
   '''
   def __init__(self,center=0,radius=0):

      self.center = center
      self.radius = radius

      
