# CPE 101 Lab 4
# Name: Bradley Weeks

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      inc = get_increment()
      show_table(table_size, first, inc)
      table_size = get_table_size()

# Obtain a valid table size from the user
def get_table_size():
   size = int(input("Enter number of rows in table (0 to end): "))

   while size < 0:
      print("Size must be non-negative.")
      size = int(input("Enter number of rows in table (0 to end): "))
      
   return size;

# Obtain the first table entry from the user 
def get_first():
   first = int(input("Enter the value of the first number in the table: "))
   
   while first < 0:
      print("First number must be non-negative.")
      first = int(input("Enter the value of the first number in the table: "))

   return first;

def get_increment():
   inc = int(input("Enter the increment between rows: "))

   while inc < 0:
      print("Increment must be non-negative.")
      inc = int(input("Enter the increment between rows: "))

   return inc;

# Display the table of cubes
def show_table(size, first,inc):
   print("A cube table of size %d will appear here starting with %d." % (size, first))
   print("Number  Cube")
   s = 0
   # Insert Loop Here
   for i in range(size):
      cube = first**3
      print("%-6d  %d" % (first, first**3))
      first = (first + inc)
      s = s + cube   

   print("The sum of cubes is:",s)   
      
if __name__ == "__main__":
   main()
