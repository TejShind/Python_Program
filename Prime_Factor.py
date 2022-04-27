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
    track1 = 0
    while number % 2 == 0:
        if track1 == 0:
            print(2)
            track1 = 1
        number = number // 2
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        track2 = 0
        while number % i == 0:
            if track2 == 0:
                print(i)
                track2 = 1
            number = number // i
    if number > 2:
        print(number)


prime_factor()
print(prime_factor.__doc__)