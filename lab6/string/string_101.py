

def str_rot_13(a_string):
   str_list = []
   ord_list = []
   final_str = []
   for i in range(len(a_string)):
      str_list.append((a_string[i]))
   for i in range(len(str_list)):
      ord_list.append(ord(str_list[i]))   
   for num in range(len(ord_list)):
      if 65 <= ord_list[num] <= 90:
         ord_list[num] = ord_list[num] + 13
         if ord_list[num] > 90:
            ord_list[num] = ord_list[num] - 26
         ord_list[num] = chr(ord_list[num])
         final_str.append(ord_list[num])
   
        
      elif 97 <= ord_list[num] <= 122:
         ord_list[num] = ord_list[num] + 13
         if ord_list[num] > 122:
            ord_list[num] = ord_list[num] - 26
         ord_list[num] = chr(ord_list[num])
         final_str.append(ord_list[num])

      else:
         ord_list[num] = chr(ord_list[num])
         final_str.append(ord_list[num])
   
   return ''.join(final_str);

def str_translate_101(a_string,char_1,char_2):
   str_list = []
   ord_list = []
   final_str = []
   for i in range(len(a_string)):
      str_list.append((a_string[i]))
   for i in range(len(str_list)):
      ord_list.append(ord(str_list[i]))
   for num in range(len(ord_list)):
     if ord_list[num] == ord(char_1):
        ord_list[num] = ord(char_2)

     ord_list[num] = chr(ord_list[num])
     final_str.append(ord_list[num])

   return ''.join(final_str);

