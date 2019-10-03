from objects import *
from math import *

def distance(p1,p2=Point()):
   return sqrt((abs(p1.x-p2.x))**2 + (abs(p1.y-p2.y)**2));
   

def distance_all(point_list):
   p2 = Point(0,0)
   distance_list = [distance(x,p2) for x in point_list]
   return distance_list;

def are_in_first_quadrant(point_list):
   return [p for p in point_list if p.x > 0 and p.y > 0]
