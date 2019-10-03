import re
import sys

ILLEGAL_RE = re.compile("[^A-Z\n]")

"""
 * Reads a pattern from standard input, computes a corresponding pattern,
 * using the provided function, and displays results of comparison between
 * patterns.
 *
 * Parameters:
 *   letter - Function to compute a letter in a pattern based on row/col
 *
 * Special Notes:  n/a
 *
"""
def comparePatterns(letter):
   pattern = readPattern(sys.stdin)
   cols_list = [len(row) for row in pattern]
   computed_pattern = buildPattern(len(pattern), cols_list, letter)
   displayResults(pattern, computed_pattern)


"""
 * Reads in the pattern from the specified input stream.
 *
 * Parameters:
 *   instream - input stream from which to read
 *
 * Return: The pattern as a list of lists
 *
 * Special Notes:  n/a
 *
"""
def readPattern(instream):
   pattern = []

   lines = list(instream)
   validateStrings(lines, ILLEGAL_RE)
   pattern = [list(line.strip()) for line in lines]
   return pattern


"""
 * Verifies that each string in the input list does not contains any
 * illegal characters.
 *
 * Parameters:
 *
 *  strings - List of strings.
 *  illegal - Compiled egular expression denoting disallowed characters.
 *
 * Return: n/a
 *
 * Special Notes:
 *
 *   Exits on following error conditions:
 *      - If any string contains a disallowed character
 *
"""
def validateStrings(strings, illegal):
   for row, string in enumerate(strings):
      match = illegal.search(string)
      if match:
         print >> (sys.stderr,
            "Unsupported character '{0}' in row {1}".format(match.group(), row))
         sys.exit(1)


"""
 * Calls the provided funciton for each row and column of the pattern and
 * populates the array with the returned values.
 *
 * Parameters:
 *
 *   rows - The number of rows.
 *   cols_list - a list of the number of columns in each row.
 *   letter - function to compute a letter in the pattern given row/col.
 *
 * Return:  List containing the computed pattern.
 *
 * Special Notes: n/a
"""
def buildPattern(rows, cols_list, letter):
   pattern = []

   for r in range(rows):
      pattern_row = []
      for c in range(cols_list[r]):
         pattern_row.append(letter(r, c))
      pattern.append(pattern_row)

   return pattern


"""
 * Compares the expected pattern with the computed pattern.
 *
 * Parameters:
 *
 *   expected - The expected pattern
 *   computed - The compute pattern
 *
 * Return: n/a
 *
 * Special Notes:
 *
 *   If the computed patterns matches the expected pattern, this function
 *   displays a "success" message. Otherwise, this function displays the
 *   computed pattern with all incorrect letters replaced with the lower-case
 *   equvalent. Any non A-Z characters will show as a '?'.
 *
 *   When there are errors, the function displays a key to how to iterpret any
 *   lower-case letters or '?' characters.
 *
"""
def displayResults(expected, computed):
   if expected == computed:
      print("\nWell done - your logic produced the specified pattern!\n")
   else:
      # Doesn't match :-(
      print("\nNot done yet - ",
         "your logic did not produce the specified pattern.\n")
      print("Below you see the expected pattern on the left and your pattern")
      print("on the right. Any '?' characters indicate that your code returned")
      print("an unexpected character. Any lower case letters indicate that")
      print("your code returned the upper-case equivalent but it did not match")
      print("the specified pattern.\n")
      print("Fix your logic and test again!\n")

      widest = max(map(len, expected))
      outString = '{0:' + str(widest) + '}'

      for row in range(len(expected)):
         # row of expected pattern
         print(outString.format(''.join(expected[row])), end='')
   
         # separation
         print("   ", end='')

         # row of computed pattern
         for col, ch in enumerate(computed[row]):
            if not ch.isupper():
               sys.stdout.write('?')
            elif expected[row][col] != ch:
               sys.stdout.write(computed[row][col].lower())
            else:
               sys.stdout.write(ch)

         print() 

      print()
