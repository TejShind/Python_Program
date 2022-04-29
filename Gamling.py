"""
@Author: Tejaswini Shinde
@Date: 2022-04-29 8.41
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title : Gambling.

"""
import random

def gambling():
     """
        Description:
            Whether the player will win or lose and the percentage of win and loss
        Parameter:
            None
        Return:
            None
    """

     inputs = [int(i) for i in input("Enter the stake,bet,goal,no.fo cases separate by comma :").split(",")]
     no_of_cases = inputs[3]
     no_of_wins = 0
     no_of_loss = 0
     for i in range(no_of_cases):
        stake = inputs[0]
        bet = inputs[1]
        goal = inputs[2]
        while stake >= bet:
            result = random.randint(0, 1)
            if result == 0:
                stake -= bet
            else:
                stake += bet
            if stake >= goal:
                no_of_wins += 1
                break
            elif stake < bet:
                no_of_loss += 1
                break
     print(f"Total no of wins {no_of_wins}")
     print(f"Percentage of win :{round(no_of_wins * 100 / (no_of_wins + no_of_loss), 2)}% ,Percentage of loss :{round(no_of_loss * 100 / (no_of_wins + no_of_loss), 2)}%")

gambling()