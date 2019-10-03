def weight_on_planets():
	weight = int(input( "What do you weigh on Earth? (In pounds?) "))
	w_onmars = weight*0.38
	print("\nOn Mars you would weigh", w_onmars, "pounds.")
	w_onjupiter = weight*2.34
	print("On Jupiter you would weigh", w_onjupiter, "pounds.")
   
   
   
if __name__ == '__main__':
   weight_on_planets()
