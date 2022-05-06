"""
@Author: Tejaswini Shinde
@Date: 2022-05-07 00:23
@Last Modified by: Tejaswini Shinde
@Last Modified time: No
@Title : Amstrong Number
"""

def armstrong(n):
    """
        Description:
            Function to Chake Number is Armstrong Or Not
        Parameter:
            Passing number 
        Return:
            Returning that Number is Armstrong or Not 
    """
    Number=n
    sum=0
    while n > 0:
        digit=n%10
        sum=sum+digit*digit*digit
        n=n//10

    if Number==sum:
        print("It is a Armstrong Number.")
    else:
        print("It is not a Armstrong numberS")



if __name__== '__main__':
    n=int(input("Enter the number: "))
    armstrong(n)