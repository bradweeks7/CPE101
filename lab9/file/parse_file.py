from sys import *
   
length = len(argv)-1

if length < 1 or length > 2:
  print("Usage: [-s]", argv[0])
  exit()

elif length > 2 and (argv[1] != '-s' or argv[2] != '-s'):
  print("Usage: [-s]", argv[0])
  exit()

try:
   if length == 1:
      InFile = open(argv[1],'r')
   elif argv[1] == '-s':
      InFile = open(argv[2], 'r')
   elif argv[2] == '-s':
      InFile = open(argv[1], 'r')
   else:
      print("usage: [-s]", argv[1])
      exit()
except Exception as e:
   if argv[1] == '-s':
      print('Unable to open ', argv[2])
      exit()
   else:
      print('Unable to open ', argv[1])
      exit()

ints = 0
floats = 0
other = 0  
s = 0

for line in InFile:
   line = line.strip()
   line_list =  line.split(' ')
   for item in line_list:
      try:
         fl =  float(item)
         if item.isdigit():
           ints += 1
           s += int(item)
         else:
           floats += 1 
           s += fl
      except Exception as e:
         if len(item):
            other += 1

if length == 2 and argv[1]  == '-s': 
   print("Ints: ", ints)
   print("Floats: ", floats)
   print("Other: ",other)
   print("Sum: ",s)

elif length == 2 and argv[2] == '-s':
   print("Ints: ", ints)
   print("Floats: ", floats)
   print("Other: ",other)
   print("Sum: ",s)
elif length == 3 and argv[2] == '-s': 
   print("Ints: ", ints)
   print("Floats: ", floats)
   print("Other: ",other)
   print("Sum: ",s)
else:
   print("Ints: ", ints)
   print("Floats: ", floats)
   print("Other: ",other)
