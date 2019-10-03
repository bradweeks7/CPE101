import driver

def letter(row,col):


   if 3 < row <= 5  and  7 <= col <=  9:
      return 'X'
   elif col > 3 and col < 10 and row > 1 and row < 6:
      return 'Z'
   elif col > 6  and col < 13 and row > 3 and row < 7:
      return 'B'
   else:
      return 'T'
if __name__ == '__main__':
   driver.comparePatterns(letter)
