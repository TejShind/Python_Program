"""
@Author: Tejaswini Shinde
@Date: 2022-04-29 22:33
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title : Prints the wind chill.

"""

if __name__ == '__main__':
    t = float(input("Enter value of  Temperature :- "))
    v = float(input("Enter value of Speed :- "))

    if t < 50 and v < 120 and v > 3:
        windChill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v**0.16)
        print("Wind Chill Is: " ,windChill)
    else:
        print("Values Are Not Valid ") 