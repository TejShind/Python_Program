"""
@Author: Tejaswini Shinde
@Date: 2022-04-27 92022:30
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

    if (year % 4) == 0:

        if (year % 100) == 0: 

            if (year % 400) == 0:
                print(year,  "Is Leap A Year")

            else:
                print(year,  "Is Not A Leap Year")

        else: 
                print(year,  "Is A Leap Year")
    else:
                print(year,  "Is Not A Leap Year") 

while True:
    checkYear = int(input("Enter a Year You Want To Check Laep Year Or Not ?"))     

    if (checkYear > 9999) or (checkYear < 1000):
        checkYear = int(input("Please, Enter Valid Year "))

    else:
        leapYearCheck(checkYear)
        break      