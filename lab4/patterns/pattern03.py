import driver

def letter(row, col):
   if col >= 10:
      return 'O'
   else:
      return 'X'

if __name__ == '__main__':
   driver.comparePatterns(letter)
