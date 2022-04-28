"""
@Author: Tejaswini Shinde
@Date: 2022-04-27 3:10
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title : Flip Coin and print percentage of Heads and Tails
"""

import random

def flip_coin():
    """
    Description:
            This function takes the no of flips as input and output the percentage of head and tails
    Parameter:
            None
    Return:
            Return the function

    """
    no_of_flips = int(input("Enter the number of times you want to flip coin :"))
    if no_of_flips < 0:
        print('Enter the positive value')
        return flip_coin()
    head = 0
    tail = 0
    for flip in range(no_of_flips):
        rand_num = random.uniform(0, 1)
        if rand_num < 0.5:
            tail += 1
        else:
            head += 1
    print(f"Percentage of heads :{round((head / (head + tail)) * 100, 2)}%")
    print(f"Percentage of tails :{round((tail / (head + tail)) * 100, 2)}%")


flip_coin()