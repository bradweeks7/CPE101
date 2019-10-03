from solverFuncs import *

cages = get_cages()
puzzle = puzzle_slate()
step = 0
checks = 0
iteration = 1
backtracks = 0
while step < 25 : 
   currentrow = step // 5
   currentcolumn = step % 5
   puzzle[currentrow][currentcolumn] = (puzzle[currentrow][currentcolumn]+1)
   next_step = check_valid(puzzle,cages)
   checks = checks + 1
   
   if next_step:
        step = step + 1        
   else:
      while puzzle[currentrow][currentcolumn] == 5:
         puzzle[currentrow][currentcolumn] = 0
         step = step - 1
         backtracks = backtracks + 1
         currentrow = step // 5
         currentcolumn = step % 5
       
    
print("\n---Solution---\n")

for x in range(len(puzzle)):
   for y in range(5):
       print(puzzle[x][y], end=' ')  #format text after finishing main loop
   print("")
print("\nchecks:", checks, "backtracks:", backtracks)
   
