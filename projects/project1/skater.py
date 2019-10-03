# Project 1
#
# Name: Bradley Weeks
# Instructor: Workman
# Section: 3

import math 
from funcs import poundsToKG
from funcs import getMassObject
from funcs import getVelocityObject
from funcs import getVelocitySkater

x = '\nNice throw!'

def main():
    pounds =  int(input('How much do you weigh (pounds)? '))
    massSkater = poundsToKG(pounds)
    distance = int(input('How far away is your professor (meters)? '))
    massObject = input('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ')
    mass = getMassObject(massObject)
    velObject = getVelocityObject(distance)
    SkaterVelocity = getVelocitySkater(massSkater, mass, velObject)
  
    if mass <= 0.1:
       print(x,"You're going to get an F!")
    elif mass > 0.1 and mass <= 1.0:
       print(x,"Make sure your professor is OK.")
    elif mass > 1.0:
        if distance < 20:
           print(x,"How far away is the hospital?")
        else:
           print(x,"RIP professor.")
    print('Velocity of skater: %.3f m/s' % SkaterVelocity)

    if SkaterVelocity < 0.2:
      print("My grandmother skates faster than you!")
    elif SkaterVelocity >= 1.0:
      print("Look out for that railing!!!")
    else:
     SkaterVelocity = 0


if __name__ == '__main__':
   main()
