
from sys import *
from pixel import *

length = len(argv)

#argument vector length analysis (checks for file)

if length < 1:
   print("Usage: python decode.py <image.ppm>")
   exit()
elif length < 3:
   print("Usage: Missing Row or Column")
   exit()
elif length < 4:
   print("Usage: Missing Radius")

elif length < 5:
   reach = 4
   row = int(argv[2])
   column = int(argv[3])
   radius = int(argv[4])

else:
   row = int(argv[2])
   column = int(argv[3])
   radius = int(argv[4])
   reach = int(argv[5])
#attempts to open file 

try:
      image = open(argv[1],'r')
      image.close()

except Exception as e:

      print('Unable to open', '<' + argv[1] + '>')
      exit()

#all file formatting

new_file = []
image = open(argv[1],'r')
image_blurred = file_name(argv[1],'_blurred.ppm')

image = open(argv[1],'r')
a_list = []

for line in image:
   line = line.strip()
   line = line.split(' ')
   for i in range(len(line)):
      a_list.append(line[i])

#end of file formatting

sep_pixels = groups_of_3(a_list[4:])
pixels = []

for i in sep_pixels:
   pixel = get_pixel(i)
   pixels.append(pixel)
   

width = int(a_list[1])
height = int(a_list[2])

#making pixels into a 2d grid based on given width and height given in ppm file

pixels2d = groups_of_x(pixels,width,height)

for i in range(len(pixels2d)):
   if (len(pixels2d[i]) != 400):
      print("Not good " + str(i) + " " + str(len(pixels2d[i])))

copied_list = list(pixels2d)
#meat of the calculations
#takes the entire 2d list of pixels, checks to see if they are in the radius of the center pixel for blurring, then from there, calculates blur factor and exports pixel to file
  

top = (row+(radius*2))
bottom = (row-(radius*2))
left = (column-(radius*2))
right = (column+(radius*2))

for y in range(height):
   for x in range(width):
      net_distance = distance(column,row,x,y)
      if net_distance <= radius*2:
        reach_multiplier = calc_reach_effect(net_distance,radius)
        nreach = int(reach*reach_multiplier)
        copied_list[y][x] = calc_pix_blur(pixels2d,nreach,x,y)      
      


image_blurred.write("P3\n" + str(width) + ' ' + str(height) + "\n" + '255' '\n')
for j in range(len(copied_list)):
   for i in copied_list[j]:
      image_blurred.write(str(i))
      image_blurred.write('\n')


image_blurred.close()
