"""
@Author: Tejaswini Shinde
@Date: 2022-04-27 23.30
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title : Harmonic Number
"""



def harmonic_number():
    """
        Description:
            Prints the nth Harmonic Number
        Parameter:
            None
        Return:
            Returning nth harmonic numebr 
    """
    number = int(input("Enter the non zero positive number to get harmonic sum :"))
    if number <= 0:
        print("Enter the non-zero positive integer")
        return harmonic_number()
    harmonic_sum = 0
    for i in range(1, number + 1):
        harmonic_sum += 1 / i
    print(f"The harmonic sum is :{harmonic_sum}")


harmonic_number()