def list_sum(a_list):
   s = [a_list]
   s = sum(a_list)
   return s;

def index_of_smallest(a_list):
   if len(a_list) > 0:
      small = a_list[0]
      for num in a_list:
         if num < small:
            small = num
   for i in range(len(a_list)):
      if a_list[i] == small:
         return i;
   else:
      return -1;
   
