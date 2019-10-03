from math import *

def get_cages():
   num_cages = int(input("Number of cages: "))
   cages = []
   v = 0
   while v < num_cages:
      v = str(v)
      cage = input("Cage number "+v+": ").split()
      cage_nums = [int(num) for num in cage]
      cages.append(cage_nums)
      v = int(v) + 1
 
   
   return cages;

def puzzle_slate():
   puzzle = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
   return puzzle;

def update_rows(puzzle):
   rows = puzzle 
   return rows;


def update_columns(puzzle):
   columns = []
   for j in range(5):
      column = []
      for i in range(5):
         column.append(puzzle[i][j]) 
      columns.append(column)
   return columns;
 
def check_rows_valid(rows):
    for i in range(5):
       row1 = rows[i].count(1)
       if row1 > 1:
          return False;
       row2 = rows[i].count(2) 
       if row2 > 1:
          return False;
       row3 = rows[i].count(3)
       if row3 > 1:
          return False;
       row4 = rows[i].count(4) 
       if row4 > 1:
          return False;
       row5 = rows[i].count(5) 
       if row5 > 1:
          return False;
    return True;

def check_cols_valid(columns):
    
   for i in range(5):
      col1 = columns[i].count(1)
      if col1 > 1:
         return False;
      col2 = columns[i].count(2) 
      if col2 > 1:
         return False;
      col3 = columns[i].count(3) 
      if col3 > 1:
         return False;
      col4 = columns[i].count(4) 
      if col4 > 1:
         return False;
      col5 = columns[i].count(5) 
      if col5 > 1:
         return False;
   return True;   
    
def check_cages_valid(puzzle,cages):

   for i in range(len(cages)):
      cage_sum = cages[i][0] #identifies cage sum
      cage_cells = cages[i][2:]  #makes a list of cells in given cages
      puzzle_cages = [puzzle[cell // 5][cell % 5] for cell in cage_cells]  
      puzzle_cage_sum = sum(puzzle_cages)
      if cage_sum <= puzzle_cage_sum and puzzle_cages.count(0) > 0: 
         return False;
      if cage_sum != puzzle_cage_sum and puzzle_cages.count(0) == 0:
         return False;
   return True; 

def check_valid(puzzle, cages):
   
   columns = update_columns(puzzle)
   rows = update_rows(puzzle) 
  
   if check_cages_valid(puzzle,cages) == True and check_cols_valid(columns) == True and check_rows_valid(rows) == True :
      return True;
   else:
      return False;

 
