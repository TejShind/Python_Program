"""
@Author: Tejaswini Shinde
@Date: 2022-04-27 2:10
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2020-04-28 13.28
@Title :Printing the String with User Name
"""


def user_name():
    """
        Description:
           Below function asks for the username and greet with the username        
        Parameter:
            None
        Return:
            None
    """

    print("Hello,How Are You! ")
#if __name__ =='__main__':

    name = input("Enter the user name :\n")
    while True:
      if len(name) < 3:
         name=input("Entert valide user name with minimum three character : \n")
      else:
          break

user_name()