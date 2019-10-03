from quakeFuncs import *

from urllib.request import *
from json import *
from datetime import *
from operator import *

choice = 'a'
earthquakes = read_quakes_from_file('quakes.txt')
display_Earthquakes(earthquakes)
choice = choose_options()

while choice != 'q' and choice != 'Q':

   if choice == 'f' or choice == 'F':
      quakes = filter_option(earthquakes)
      display_Earthquakes(quakes)

   if choice == 'n' or choice == 'N':

      dictionary = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
      new_earthquakes = [quake_from_feature(feature) for feature in dictionary["features"]]

      for quakes in new_earthquakes:
         added = 0
         if quakes not in earthquakes:
            earthquakes.append(quakes) 
            added += 1
      
      if added > 0:
         print()
         print("New quakes found!!!")
      
      print()
      display_Earthquakes(earthquakes)
   
   if choice == 's' or choice == 'S': 
      earthquakes = sort_option(earthquakes)
      display_Earthquakes(earthquakes)
   
   choice = choose_options()

write_final_e('quakes.txt', earthquakes)

