"""
@Author: Tejaswini Shinde
@Date: 2022-04-27 2:10
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title :Printing the String with User Name
"""

"""
  Description:
            Below function asks for the username and greet with the username
        Parameter:
            None
        Return:
            None


"""


def user_name():
    name = input("Enter the name :")
    if len(name) >= 3:
        print(f"Hello {name}, how are you ?")


user_name()