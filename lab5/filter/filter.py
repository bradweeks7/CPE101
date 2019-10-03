def are_positive(x):
   positive_list = []
   i = 0 
   while i < len(x):
      if x[i] > 0:
         positive_list.append(x[i])
      i = i+1
   
   return positive_list;

def are_greater_than_n(x,n):
   greater_than = []
   
   for num in x:
      if num > n:
         greater_than.append(num)
      
   return greater_than;


def are_divisible_by_n(big_list, number):
   divisible_by = [num for num in big_list if num/number == int(num/number)]
   return divisible_by;
