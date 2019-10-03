from funcs import *

#Accquiring Data and Parsing

puzzleStr = input()
words = input().split()
puzzle = []
reversepuzzle = []
puzzlebackwards  = puzzleStr[::-1]
F = "(FORWARD)"
D = "(DOWN)"
DIA = "(DIAGONAL)"
U = "(UP)"
B = "(BACKWARD)"

for i in range(0,100,10):
   puzzle.append(puzzleStr[i:i+10])

for i in range(0,100,10):
   reversepuzzle.append(puzzlebackwards[i:i+10])

 
reversecolumns = get_columns(reversepuzzle)
columns = get_columns(puzzle)
diagonals = get_diagonals(puzzle,columns)

#Printing the Puzzle and Solution Segment

print("Puzzle:\n")
for i in puzzle:
   print(i)
        
#Checking where words lie in the puzzle       
print()

for word in words:
   row = check_row(puzzle,word)
   column = check_column(columns,word)
   Rrow = check_row(reversepuzzle,word)
   Rcolumn = check_column(reversecolumns,word)
   diagonal = diagonal_search(diagonals, word)
   if row != None :
      print(word+":", F, "row:", row[0], "column:",row[1])
   elif column != None:
      print(word+":", D, "row:", column[0], "column:", column[1])
   elif Rrow != None :
      print(word+":", B, "row:", 9-Rrow[0], "column:", 9-Rrow[1])
   elif Rcolumn != None :
      print(word+":", U, "row:", 9-Rcolumn[0], "column:", 9-Rcolumn[1])
   elif diagonal != None :
      print(word+":", DIA, "row:", diagonal[0], "column:", diagonal[1])
   elif row ==  None and column == None and Rrow == None and Rcolumn == None :
      print(word+": word not found")
