"""
@Author: Tejaswini Shinde
@Date: 2022-04-28 8.30
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title : Prime Factor
"""

import math


def prime_factor():
    """
        Description:
            Gives the prime factor of given number
        Parameter:
            None
        Return:
            Returning nothing but printing factors
    """

    number = int(input("Enter the positive number to find its prime factor :"))
    if number == 0 or number == 1:
        print(f"{number} has no prime factor")
        return
    num1 = 0
    while number % 2 == 0:
        if num1 == 0:
            print(2)
            num1 = 1
        number = number // 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        num2 = 0
        while number % i == 0:
            if num2 == 0:
                print(i)
                num2 = 1
            number = number // i
    if number > 2:
        print(number)


prime_factor()
