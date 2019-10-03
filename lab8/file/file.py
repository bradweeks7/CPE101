inFile = open('in.txt','r')
outFile = open('out.txt','w')

line_num = 0

for line in inFile:
   line = line.strip()
   outFile.write("Line " + str(line_num) + ' (' + str(len(str(line))) + ' chars): ' + line + "\n")
   line_num += 1
