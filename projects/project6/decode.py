from sys import *
from encodeFuncs import *
from pixel import *

length = len(argv)-1


if length < 1:
  print("Usage: python encode.py <image.ppm>")
  exit()

try:
      image = open(argv[-1],'r')
      image.close()

except Exception as e:

      print('Unable to open', '<' + argv[-1] + '>')
      exit()

new_file = []
image = open(argv[-1],'r')
image_decode_data = file_decode_name(argv[-1],'_decoded.ppm')

image = open(argv[-1],'r')
a_list = []

for line in image:
   line = line.strip()
   line = line.split(' ')
   for i in range(len(line)):
      a_list.append(line[i])


sep_pixels = groups_of_3(a_list[4:])
pixels = []
pixels.append(a_list[:4])

for i in sep_pixels:
   pixel = get_pixel(i)
   pixels.append(pixel)

width = pixels[0][1]
height = pixels[0][2]

decoded_pixels = []

for i in range(len(pixels[1:])):
   column = i % int(height)
   row  = i % int(width)
   decoded_pixels.append(decode_pixel(pixels[i+1],row,column))

image_decode_data.write("P3\n" + str(width) + str(height) + "\n" + '255'+ '\n')
for i in decoded_pixels:
   image_decode_data.write(str(i))
   image_decode_data.write('\n')

image_decode_data.close()