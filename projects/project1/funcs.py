import math

def Distance():
  distance = int(input('How far away is your professor (meters)?'))

def poundsToKG(pounds):
    kilograms = pounds*0.453592
    return kilograms

def getMassObject(massObject):
    if massObject == 't':
        mass = 0.1
    elif massObject == 'p':
        mass = 1.0
    elif massObject == 'r':
        mass = 3.0
    elif massObject == 'g':
        mass = 5.3
    elif massObject == 'l':
        mass = 9.07
    else:
        mass = 0.0

    return mass

def getVelocityObject(distance):
    velObject  = float(math.sqrt((9.8*distance)/2))
    return velObject

def getVelocitySkater(kilograms, mass, velObject):
    SkaterVelocity = float((mass*velObject)/kilograms)
    return SkaterVelocity 

