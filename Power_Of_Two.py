"""
@Author: Tejaswini Shinde
@Date: 2022-04-27 22.49
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-04-29
@Title : Power Of two
"""
def power_of_two(n):
    """
    Description: 
       It gives the power of two of the numbers till given input number
    Parameter:
        Passing power value of n
    Return:
        Returning power of 2 until n value
    """
    for i in range(number+1):
        print(2 ** i) 


number = int(input("Enter the number of time you want to calculate power: "))
if (number <= 0) or (number >31):
    print("Enter a valid Range")

else:
       power_of_two(number)