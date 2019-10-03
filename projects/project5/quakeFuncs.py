from urllib.request import *
from json import *
from datetime import *
from operator import *

# FUNCTIONS:
# Use these two as-is and do not change them
def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    
   
# Earthquake class definition here   

class Earthquake:

   ''' Stores Earthquake data in a class with 5 pieces of data 
    Place - string
    Magnitude - float  
    Longitude - float
    Latitude - float
    Time - Int
   '''
   def __init__(self,place='',mag=0.0,longitude=0.0,latitude=0.0,time=0):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   def __eq__(self,other):
      return self.place == other.place and self.mag == other.mag and \
             self.longitude == other.longitude and \
             self.latitude == other.latitude and self.time == other.time

   def epsilon_equal(n, m, epsilon=0.00001):
      return (n - epsilon) < m and (n + epsilon > m)

   #def __str__(self):
    #  return (self.place + ',' + self.mag + ',' + self.longitude + ',' + self.latitude + ',' + self.time)  
  
   

   def __repr__(self):
      print(self.place)
      return str(self.place) + " " + str(self.mag) + " " + str(self.longitude) + " " + str(self.latitude) + " " + str(self.time)


# Required function - implement me!   
def read_quakes_from_file(filename):  
   inFile = open(filename,'r')
   line_num = 0
   earthquakes = []
   for line in inFile:
      line = line.strip().split()
      place = " ".join(line[4:])
      mag = float(line[0])
      longitude = float(line[1])
      latitude = float(line[2])
      time = int(line[3])
      
      earthquakes.append(Earthquake(place,mag,longitude,latitude,time))
      line_num += 1

   inFile.close()

   return earthquakes;

def write_final_e(outfile, earthquakes):
   outfile = open(outfile, 'w')
   formatting = []
   for item in earthquakes:
      formatting.append(str(item.mag) + ' ' + str(item.longitude) + ' ' + str(item.latitude) + " " + str(item.time) + " " + str(item.place))
   for item in formatting:
      outfile.write(item+"\n")

   outfile.truncate()
   outfile.close()
   
      
   

def display_Earthquakes(earthquakes):
   print("Earthquakes:")
   print("------------")  
   display_earthquake_data(earthquakes)
   print()
   print("Options:")
   print("   (s)ort")
   print("   (f)ilter")
   print("   (n)ew quakes")
   print("   (q)uit")
   print()


def choose_options():
   choice = input("Choice: ").strip()
   return choice;
  
def filter_option(earthquakes):
      filt = input(("Filter by (m)agnitude or (p)lace? ")).strip()
      if filt == 'm' or filt == 'M':
         low = float(input("Lower bound: ").strip())
         high = float(input("Upper bound: ").strip())
         quakes = filter_by_mag(earthquakes,low,high)
      if filt == 'p' or filt == 'P':
         word = input("Search for what string? ").strip()
         quakes = filter_by_place(earthquakes,word) 
      print() 
      return quakes;

def new_quakes_option(earthquakes):
   if choice == 'n' or choice == 'N':
      print()
      print("New quakes found!!!")
      get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson') 

def sort_option(earthquakes):
      sor = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ").strip()
      if sor == 'm' or sor == 'M':
         quakes = sorted(earthquakes, key=lambda x: x.mag, reverse=True)
      if sor == 't' or sor == 'T':
         quakes = sorted(earthquakes, key=lambda x: x.time, reverse=True)
      if sor == 'l' or sor == 'L':
         quakes = sorted(earthquakes, key=lambda x: x.longitude, reverse=False)
      if sor == 'a' or sor == 'A': 
         quakes = sorted(earthquakes, key=lambda x: x.latitude, reverse=False)
      print()
      return quakes;

# Required function - implement me!
def filter_by_mag(quakes, low, high):
   mag_quakes = [quakes[i] for i in range(len(quakes)) if (low <= quakes[i].mag <= high)]
   return mag_quakes;
          
     
# Required function - implement me!
def filter_by_place(quakes, word):
   quakes_place = [] 
   for i in quakes:
         if word.lower() in i.place.lower():
            quakes_place.append(i)
   return quakes_place;

# Required function for final part - implement me too!   
def quake_from_feature(feature):
   a_quake = Earthquake(feature["properties"]["place"],feature["properties"]["mag"],  feature["geometry"]["coordinates"][0], feature["geometry"]["coordinates"][1], int((feature["properties"]["time"])/1000))
   return a_quake;
     
def display_earthquake_data(earthquakes):
   for earthquake in earthquakes:
      print('(%.2f)' % earthquake.mag, '%40s' % earthquake.place, "at", time_to_str(earthquake.time), '(%8.3f,' % earthquake.longitude, '%6.3f)' % earthquake.latitude)
    
