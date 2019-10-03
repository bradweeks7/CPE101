import driver 

def letter(row,col):
   if row <= 9:
      return 'R'
   else:
      return 'Q'


if __name__ == '__main__':
   driver.comparePatterns(letter)
