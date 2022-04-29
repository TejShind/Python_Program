"""
@Author: Tejaswini Shinde
@Date: 2022-04-29 8:20
@Last Modified by: Tejaswini Shinde
@Last Modified time: 4:20
@Title : Gambling.

"""
import random

def gambling(stack,goal,no_of_trial):
     """
        Description:
            Whether the player play the Gambler game
        Parameter:
            Passing value of stake goal and number of times trial
        Return:
            Return win or losethe percentage of win and loss
    """

     bet=0
     no_of_wins = 0
     for i in range(no_of_trial):

        win=0
        doller=stack
        while doller > 0 and doller < goal:
            bet+=1
            result = random.randint(0, 1)
            if result == win:
                doller += 1
            else:
                doller -= 1
            if doller == goal:
                no_of_wins += 1
              
     percentageOfWin=(no_of_wins/no_of_trial)*100
     print("Percentage of win : ", percentageOfWin)
     print("Percentage of loss : ", 100-percentageOfWin)

stack =int (input("Enter the value od Stack: "))
goal=int(input("Enter the goal :"))
no_of_trial=int(input("Enter number of time you want to trial:"))
gambling(stack,goal,no_of_trial)