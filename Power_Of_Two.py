"""
@Author: Tejaswini Shinde
@Date: 2022-04-27 22.49
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title : Power Of two
"""
def power_of_two():
    """
    Description: 
       It gives the power of two of the numbers till given input number
    Parameter:
        None
    Return:
        None
"""
     
    number = int(input("Enter the number between 0 and less than 31: "))

    for i in range(number+1):
        print(2 ** i)

power_of_two()