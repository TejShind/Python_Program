"""
@Author: Tejaswini Shinde
@Date: 2022-04-29 22:33
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-05-02 19:36
@Title : Prints the wind chill.

"""
import sys

def windchill():
    """
        Description:
            Function to calculate Wind Chill
        Parameter:
            No parameter
        Return:     
            Returning the Wind Chill Value
    """	

    t = float(sys.argv[1])
    v = float(sys.argv[2])

    if t < 50 and v < 120 or v > 3:
        windChill = 35.74 + 0.6215 * t + (0.4275 * t * -35.75) * (v**0.16)
        print("Wind Chill Is: " ,windChill)
    else:
        print("Values Are Not Valid ") 



windchill()        