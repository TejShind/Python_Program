"""
@Author: Tejaswini Shinde
@Date: 2022-04-27 22.49
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title : Leap Year
"""

def leapYearCheck(year):
    """
        Description:
            Print the year is a Leap Year or not.
        Parameter:
            Passing int variable as year
        Return:
            Returning Nohting but printing statement year is leap or Not
    """
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));
 
year = int(input("Enter the year :"))

if(leapYearCheck(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")

   