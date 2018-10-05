"""
ICS 32 Project 3
Author: Lillian Pham
UCI_ID: 68168196
"""

"""
This module implements the various outputs
    -Each kind of output that can be generated by the program must be
    implemented as a separate CLASS
    -All of the classes must have the same name, same parameters, same return type
"""

class STEPS:
    """
    Prints the directions the user needs to follow in order
    to reach the destination(s)
    """
    def __init__(self, steps: [str]):
        self.steps = steps
        
    def generate_output(self):
        print("\nDIRECTIONS")
        for step in self.steps:
            print(step)

class TOTALDISTANCE:
    """
    Prints the total distance needed to travel to reach the
    destination(s)
    """
    def __init__(self, total_distance: int):
        self.total_distance = total_distance
        
    def generate_output(self):
        print("\nTOTAL DISTANCE:", self.total_distance, "miles")

class TOTALTIME:
    """
    Prints the total time it takes to complete the trip
    """
    def __init__(self, total_time: int):
        self.total_time = total_time
        
    def generate_output(self):
        print("\nTOTAL TIME:", self.total_time, "minutes")

class LATLONG:
    """
    Prints the latitude and longitude of each location specified
    by the user
    """
    def __init__(self, latlong: [dict]):
        self.latlong = latlong
        
    def generate_output(self):
        print("\nLATLONGS")
        for dic in self.latlong:
            latitude = str(round(dic["lat"], 2))
            longitude = str(round(dic["lng"], 2))
            if latitude.startswith("-"):
                latitude = (latitude + "S").replace("-", "")
            else:
                latitude = latitude + "N"
            if longitude.startswith("-"):
                longitude = (longitude + "W").replace("-", "")
            else:
                longitude = longitude + "E"
            print(latitude, longitude)
    
class ELEVATION:
    """
    Prints the elevation of each location
    """
    def __init__(self, elevation: [int]):
        self.elevation = elevation
        
    def generate_output(self):
        for elevation in self.elevation:
            print(elevation)