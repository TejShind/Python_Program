"""
@Author: Tejaswini Shinde
@Date: 2022-04-28 17:36
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-04-29 15:15
@Title : Calculate distance between of x and y co-ordinator from origin

"""
import math

if __name__ == '__main__':

    x1=0
    y1=0

    x2=int(input("Enter x co-ordinate"))
    y2=int(input("Enter y co-ordinate"))

    Distance = math.sqrt((x2*x2)+(y2*y2))
    print("Distance between two co-ordinates is : ",Distance )