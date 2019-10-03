from objects import *
from math import *

def distance(p1,p2):
   return sqrt((abs(p1.x-p2.x))**2 + (abs(p1.y-p2.y)**2));

def circles_overlap(c1,c2):
     # c = Center((Point(x,y), Radius) 
   D = distance(c1.center,c2.center)
   r1 = c1.radius
   r2 = c2.radius
   R = r1+r2

   return R > D;
