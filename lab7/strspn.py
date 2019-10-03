def my_strspn(str1,str2):
   count = 0
   for i in range(len(str1)):
         if str1[i] in str2:
            count += 1   
         else:
            break
      
   return count;  

def main():
   str1 = input("Enter string1: ")
   str2 = input("Enter string2: ")
   result = my_strspn(str1,str2)
   print("Result:",   result)
