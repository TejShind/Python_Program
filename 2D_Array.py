"""
@Author: Tejaswini Shinde
@Date: 2022-04-28 16.57
@Last Modified by: Tejaswini Shinde
@Last Modified time: 2022-04-28 14.25
@Title : Print 2D array
"""

def two_dim_array():
    """
        Description:
            Adding values in 2D Array
        Parameter:
            None
        Return:
            None
    """
    inputs = [int(i) for i in input("Enter the no of rows , columns separate by comma :").split(",")]
    elements = input("Enter the (rows X colums) elements separated by comma :").split(",")
    rows = input[0]
    colums= input[1]  
    two_dim_array=[]
    for i in range(rows):  
        one_dim_array =[]
        for j in range(colums):
            one_dim_array.append(elements[i*colums+j])
        two_dim_array.append(one_dim_array)
    print(two_dim_array)
two_dim_array()
   