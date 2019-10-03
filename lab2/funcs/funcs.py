import math
def f(x):
	output = 7*(x**2)+2*(x)
	return output

def g(x,y):
	output = ((x**2)+(y**2))/(3*x)
	return output

def hypotenuse(x,y):
	length = math.sqrt((x**2)+(y**2))
	return length

def is_positive(x):
	value = x
	return(value >= 0)
	

