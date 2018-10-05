"""
This module interacts with the Open MapQuest APIs
    -Builds URLs, makes HTTP requests, parses JSON responses, etc
"""

import http.client

import urllib.request
import urllib.parse
import urllib.error

import json

API_KEY = "b4nfJRNmg1fh1HZ2ZoiOTgyGIiiGFLmv"

def build_directions_url(locations: [str]) -> str:
    """
    Takes in a list of the specified locations to build the URL
    of the Open Directions API and returns a list of the URLs
    """
    base_url = "http://open.mapquestapi.com/directions/v2/route?"
    query_parameters = [("key", API_KEY)]
    
    for i in range(len(locations[:-1])):
        query_parameters.append(("from", locations[i]))
        query_parameters.append(("to", locations[i+1]))
        
    return base_url + urllib.parse.urlencode(query_parameters)

def build_elevation_url(result: dict) -> [str]:
    """
    Builds the URL of the Open Elevation API and returns a list of the URLs
    """
    base_url = "http://open.mapquestapi.com/elevation/v1/profile?"
    latLng_list = latLng(result)
    URLs = []
    
    for dic in latLng_list:
        query_parameters = [
            ("key", API_KEY), (("latLngCollection", str(dic["lat"]) + "," + str(dic["lng"]))),
            ("unit", "f")
            ]
        URLs.append(base_url + urllib.parse.urlencode(query_parameters))
        
    return URLs

def get_result(URL: str) -> dict:
    """
    Takes in a list of URLs and returns a Python dictionary that represents
    the parsed JSON response
    """
    response = None
    loaded_text = []
    
    try:
        response = urllib.request.urlopen(URL)
        json_text = response.read().decode(encoding = "utf-8")
        return json.loads(json_text)
    
    except urllib.error.URLError:
        print("\nMAPQUEST ERROR")
        
    finally:
        if response != None:
            response.close()

def steps(result: dict) -> [str]:
    """
    Returns the steps needed to get to the destination as a list
    """
    steps = []
    
    for dic in result["route"]["legs"]:
        for sub_dic in dic["maneuvers"]:
            steps.append(sub_dic["narrative"])
            
    return steps

def total_distance(result: dict) -> float:
    """
    Returns the total distance needed to travel to get to the destination
    """
    total_distance = 0
    total_distance += result["route"]["distance"]
    return round(total_distance)

def total_time(result: dict) -> int:
    """
    Returns the total amount of time it takes to complete the trip
    """
    total_time = 0
    total_time += result["route"]["time"] / 60
    return round(total_time)
    
def latLng(result: dict) -> [dict]:
    """
    Returns a list of dictionaries. Each dictionary contains the latitude and
    longitude of each location specified by the user
    """
    latLng_list = []
    
    for dic in result["route"]["locations"]:
        latLng_list.append(dic["latLng"])
        
    return latLng_list

def elevation(result: dict) -> [int]:
    """
    Returns a list of integers that represent the elevation of each location
    """
    elevations = []
    
    for dic in result["elevationProfile"]:
        elevations.append(round(dic["height"]))
        
    return elevations
