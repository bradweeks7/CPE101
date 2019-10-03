def square_all(square_list):
   nums = [] 
   for num in square_list:
      nums.append(num**2)
   return nums;
   
def add_n_all(n,a_list):
   b_list = [n+num for num in a_list]
   return b_list;

def even_or_odd_all(int_list):
   tf_list = []
   i = 0
   while i < len(int_list):
      tf_list.append(int_list[i] % 2 == 0)
      i = i+1
   return tf_list;
