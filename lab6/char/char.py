def is_lower_101(x):
   x = ord(x)
   if 65 <= x <= 90:
      return False;
   elif 97 <= x <= 122:
      return True;
   else:
      return False;

def char_rot_13(x):
   x = ord(x)
   if 65 <= x <= 90:
      x = x + 13
      if x > 90:
         x = x - 26
      x = chr(x)
      return x;

   elif 97 <= x <= 122:
      x = x + 13
      if x > 122:
         x = x - 26
      x = chr(x)
      return x;


   else:
      x = chr(x)
      return x;
   
