"""
This module reads the input and constructs the objects that will generate
the program's output
"""

import open_mapquest_apis as api
import output_implementations as output

def read_locations() -> [str]:
    """
    Accepts the user's input for starting and ending locations
    and returns a list of the locations
    """
    num_of_locations = int(input())
    locations = []

    for i in range(num_of_locations):
        location = input()
        locations.append(location)
 
    return locations

def read_requested_outputs() -> [str]:
    """
    Accepts the requested output from the user and returns a list of
    those outputs
    """
    num_of_outputs = int(input())
    outputs = []
    
    for i in range(num_of_outputs):
        output = input().upper()
        outputs.append(output)

    return outputs

def print_steps(result: dict) -> None:
    """
    Constructs an object by calling class STEPS from module
    output_implementations.py and generates the output for STEPS
    """
    s = api.steps(result)
    steps = output.STEPS(s)
    steps.generate_output()

def print_total_distance(result: dict) -> None:
    """
    Constructs an object by calling class TOTALDISTANCE from module
    output_implementations.py and generates the output for TOTALDISTANCE
    """
    d = api.total_distance(result)
    total_distance = output.TOTALDISTANCE(d)
    total_distance.generate_output()

def print_total_time(result: dict) -> None:
    """
    Constructs an object by calling class TOTALTIME from module
    output_implementations.py and generates the output for TOTALTIME
    """
    t = api.total_time(result)
    total_time = output.TOTALTIME(t)
    total_time.generate_output()

def print_latLng(result: dict) -> None:
    """
    Constructs an object by calling class LATLONG from module
    output_implementations.py and generates the output for LATLONG
    """
    l = api.latLng(result)
    latLng = output.LATLONG(l)
    latLng.generate_output()

def print_elevation(result: dict) -> None:
    """
    Constructs an object by calling class ELEVATION from module
    output_implementations.py and generates the output for ELEVATION
    """
    e = api.elevation(result)
    elevation = output.ELEVATION(e)
    elevation.generate_output()
    
def print_requested_outputs(requested_outputs: list, result: dict) -> None:
    """
    Checks the output specified by the user and calls the appropriate
    print function
    """
    for output in requested_outputs:
        if output == "STEPS":
            print_steps(result)
        elif output == "TOTALDISTANCE":
            print_total_distance(result)
        elif output == "TOTALTIME":
            print_total_time(result)
        elif output == "LATLONG":
            print_latLng(result)
        elif output == "ELEVATION":
            elevation_urls = api.build_elevation_url(result)
            print("\nELEVATIONS")
            for url in elevation_urls:
                elevation_result = api.get_result(url)
                print_elevation(elevation_result)

def run_navigation_system():
    """
    This is the main function that runs the entire navigation system
    """
    try:
        locations = read_locations()
        requested_outputs = read_requested_outputs()
        directions_url = api.build_directions_url(locations)
        result = api.get_result(directions_url)
        print_requested_outputs(requested_outputs, result)
        
    except KeyError:
        print("\nNO ROUTE FOUND.")
        
    finally:
        print("\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.") 

if __name__ == "__main__":
    run_navigation_system()
