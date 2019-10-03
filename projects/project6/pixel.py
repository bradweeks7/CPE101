from math import *
from string import *

class Pixel:
   '''All from 0 < x < 255
      Red = Int
      Green = Int
      Blue = Float
   '''
   def __init__(self,red,green,blue):
      self.red = red
      self.green = green
      self.blue = blue

   def __eq__(self,other):
      return self.red == other.red and self.green == other.green and \
             self.blue == other.blue

   def __repr__(self):
      return '%s %s %s' % (self.red,self.green,self.blue)

   def __str_(self):
      return "%s %s %s" % (self.red,self.green,self.blue)

class Point:
   ''' two int points
   x - float
   y - float
   '''

   def __init__(self,x,y):
      self.x = x
      self.y = y
   def __eq__(self,other):
      return self.x == other.x and self.y == other.y

   def __repr__(self):
      return '%s %s' % (self.x,self.y)

   def __str__(self):
      return '%s %s' % (self.x,self.y)


def make_file_into_list(filename):
   inFile = open(filename,'r')
   pixels  = []
   for line in inFile:
      line = line.strip().split(' ')
      pixels.append(line)
      
   inFile.close()

def file_name(a_file,newname):
   new_file = []
   image = open(a_file,'r')

# naming new file based on input section
   x = 0
   for i in range(len(a_file)):
      if a_file[i] != '.' and x != 2:
         new_file.append(a_file[i])
         if a_file[i] == '_':
            x += 1
      else:
         break
   new_file = ''.join(new_file)
   file_name = new_file

   image_encoded = open(file_name + newname,'w')

   return image_encoded;

def file_decode_name(a_file,newname):
   new_file = []
   image = open(a_file,'r')
# naming new file based on input section
   for i in range(len(a_file)):
      new_file.append(a_file[i])
   new_file = ''.join(new_file)
   new_file = new_file.replace('_encoded','')
   file_name = new_file
   image_decoded = open(file_name + newname,'w')

   return image_decoded;


def get_pixel(index):
   pixel = Pixel(index[0],index[1],index[2])
   return pixel;
   
def groups_of_3(alist):
   big_list = [alist[i:i+3] for i in range(0,len(alist),3)]
   return big_list;

def groups_of_x(alist,rowlen,rows):
   list2d = [alist[i:i+int(rowlen)] for i in range(0,len(alist),int(rows))]
   return list2d;

def is_in_radius(row,column,x,y):
   pass
  

def encode_pixel(p,row,column):
   nred = int(p.green) * (int(column)+3) * (int(row)+5)
   ngreen = int(p.blue) * ( ( (int(column)+3) * (int(row) + 5)) ** 2)
   nblue = int(p.red) * (((int(column)+3)*(int(row)+5)) ** 3)
   return Pixel(nred,ngreen,nblue);

def decode_pixel(p,row,column):
   red = int(int(p.blue)/(((int(column)+3)*(int(row)+5))**2))
   blue = int(int(p.green)/(((int(column)+3)*(int(row)+5))**3))
   green = int(int(p.red)/((int(column)+3)*(int(row)+5)))
   return Pixel(red,green,blue)  

def distance(p1x,p1y,p2x,p2y):
   dist = sqrt((p1x-p2x)**2 + (p1y-p2y)**2)
   return dist

def calc_reach_effect(net_distance,radius):
   reach_effect = (1-(net_distance - radius)/radius)
   if reach_effect <= 0:
      reach_effect = 1
   return reach_effect;

def calc_pix_blur(pixels2d,reach,x,y):
   if reach == 0:
     return pixels2d[y][x];

   pred = []
   pgreen = []
   pblue = []

   for i in range(reach):
      for j in range(reach):
         pred.append(int(pixels2d[y+i][x+j].red))
         pgreen.append(int(pixels2d[y+i][x+j].green))
         pblue.append(int(pixels2d[y+i][x+j].blue))
      
   rpix = 0
   gpix = 0
   bpix = 0
      
   n = len(pred)
   rpix = sum(pred)
   gpix = sum(pgreen)
   bpix = sum(pblue)

     # for pix in range(n):
        # print('this is wrong'+str(rpix)+pixels_in_reach[pix].red)
    #     rpix += int(pixels_in_reach[pix].red)
    
        
   return Pixel(int(rpix/n),int(gpix/n),int(bpix/n)) 
   
    
   
   
   
   
   
