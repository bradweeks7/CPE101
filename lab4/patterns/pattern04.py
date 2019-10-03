import driver 

def letter(row,col):
  
   if row == 0 or row == 1 or row == 5 or row == 6:
      return 'S'
   elif col == 0 or col == 1 or col ==2 or col ==7 or col == 8 or col ==9:
      return 'S'
   else:
      return 'M'

if __name__ == '__main__':
   driver.comparePatterns(letter)           
