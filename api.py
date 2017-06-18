"""
API learning project. 

We want to learn how to grab raw data from publicly
availabe data by accesing it via API, parse the data and make 
a graph with help of matplotlib
"""

from __future__ import print_function
import requests

CPI_DATA_URL = "http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt"

def main():
    """This function handles the logic of this script"""

    #Grab CPI/inflation data

    #Grab API/game platform data

    #Figure out the current price of each platform.
    #This will require looping through each game platform we received,
    #and calculate the adjusted price based on the CPI data we also
    #received.
    #During this point we also validate our data so we do not skew
    #our results.

    #Generate a plot/bar graph for adjusted price data.

    #Generate a CSV file to save for the adjusted price data.