def groups_of_3(listofvalues):
   big_list = [listofvalues[i:i+3] for i in range(0,len(listofvalues),3)]
   return big_list;
         
