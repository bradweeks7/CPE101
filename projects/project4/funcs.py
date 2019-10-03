def get_columns(puzzle):
   columns = []
   for j in range(10):
      column = []
      for i in range(10):
         column.append(puzzle[i][j])
      columns.append("".join(column))
   return columns;
  

  
def check_row(puzzle,word):
   for r in range(len(puzzle)):
      row = puzzle[r]
      c = row.find(word)
      if word in row:
         return (r,c);   



def check_column(columns, word):
   for c in range(len(columns)):
      column = columns[c]
      r = column.find(word)
      if word in column:
         return (r,c);

def get_diagonals(puzzle, columns):
   diagonals = []

   for i in range(len(puzzle[0])):
      diagonal = []
      x = i
      y = 0
      while x < 10:
         diagonal.append(puzzle[y][x])
         x += 1
         y += 1
      diagonals.append("".join(diagonal))
 
   for i in range(1,10):
      diagonal = []
      x = 0
      y = i
      while y < 10:
         diagonal.append("".join(columns[x][y]))
         x += 1
         y += 1 
      diagonals.append("".join(diagonal))
    
   return diagonals;   

def diagonal_search(diagonals,word):
   for c in range(len(diagonals)):

      if c <= 9:
         row = diagonals[c]
         r = row.find(word)
         if word in row:
            return (r,(r+c));

      if c > 9:
         row = diagonals[c]
         r = row.find(word)
         if word in row:
            return (c-9+r,r);

        
