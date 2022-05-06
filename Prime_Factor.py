"""
@Author: Tejaswini Shinde
@Date: 2022-04-28 8.30
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-05-02 10:44
@Title : Prime Factor
"""

import math


def prime_factor(n):
    """
        Description:
            Gives the prime factor of given number
        Parameter:
            Passing number n
        Return:
            Returning prime factor od n value
    """

    factors=[]
    i=2
    while(i <= n):
        if(n % i == 0):
            factors.append(i)
            n=n/i
            
        else:
            i+=1 

    return factors   

n = int(input("Enter any Number for calculating the prime factors: "))

print(prime_factor(n))
