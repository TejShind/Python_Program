"""
@Author: Tejaswini Shinde
@Date: 2022-04-28 16.57
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title : Print 2D array
"""

def two_dim_array(rows,colums):
    """
        Description:
            adding values in 2D Array
        Parameter:
            Rows and Colums
        Return:
            None
    """

    array = []  
    for i in range(rows):  
        row = []  
        for j in range(colums):
            num = int(input("Enter the matrix"))  
            row.append(num)  
        array.append(row)

    for i in array:
        for j in i:
            print(j, end=" ")
        print()

two_dim_array(4,2)
   