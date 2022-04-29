"""
@Author: Tejaswini Shinde
@Date: 2022-04-27 22.49
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-04-28 16.06
@Title : Leap Year
"""

def leapYearCheck(year):
    """
        Description:
            Print the year is a Leap Year or not.
        Parameter:
            Passing int variable as year
        Return:
            Returning true if year is a multiple of 4 and not multiple of 100, OR year is multiple of 400
    """
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));
 
year = int(input("Enter the year :"))

if(leapYearCheck(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")

   