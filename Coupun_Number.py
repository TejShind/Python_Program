"""
@Author: Tejaswini Shinde
@Date: 2022-04-28 17:36
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-04-29 15:15
@Title : Coupon number.

"""
import random

def distinct_coupen_number(n):
    """
        Description:
            Function to Generate Distinct Coupon Number
        Parameter:
            Passing number of  coupon Digit.
        Return:   
            returning Distinct Coupon Number.
    """	
    list=[]
    i=1
    while i<(n+1):
        ran= random.randint(0,9)
        if ran in list: 
            i-=1
        else:
            list.append(ran)

        i+=1
    #print("Cupon Code is : " *list)
    print(" ".join(map(str, list)))
n =int(input("Enter how many digit of coupon codes you need: "))
distinct_coupen_number(n)