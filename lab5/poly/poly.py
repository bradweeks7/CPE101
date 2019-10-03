
def poly_add2(poly1, poly2):
   poly3 = []
   poly3.append(poly1[0] + poly2[0])
   poly3.append(poly1[1] + poly2[1])
   poly3.append(poly1[2] + poly2[2])
  
   return poly3;

def poly_mult2(poly1, poly2):
   poly3 = []
   poly3.append(poly1[0]*poly2[0])
   poly3.append((poly1[0]*poly2[1])+(poly1[1]*poly2[0]))
   poly3.append((poly1[0]*poly2[2])+(poly1[1]*poly2[1])+(poly1[2]*poly2[0]))
   poly3.append((poly1[1]*poly2[2])+(poly1[2]*poly2[1]))
   poly3.append(poly1[2]*poly2[2])

   return poly3;
