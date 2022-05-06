"""
@Author: Tejaswini Shinde
@Date: 2022-04-29 19:00 
@Last Modified by: Tejaswini Shinde
@Last Modified time: None
@Title : Quadratic to calculate roots

"""
import math

if __name__ == '__main__':

    a=int(input("Enter a Value of a"))
    b=int(input("Enter a Value of b"))
    c=int(input("Enter a Value of c"))

    delta = ((b*b)-4*a*c)
    print("delta",delta)

    if (delta < 0):
        print("Roots are Imaginary")
    elif (delta >0 ):
        root1 = (-b + math.sqrt(delta / (2 * a)))
        root2 = (-b - math.sqrt(delta / (2 * a)))
        print("Root 1 Is: ", root1)
        print("Root 2 Is: ", root2)

    elif (delta == 0):
        root1 = (-b / 2 * a)
        root2 = (-b / 2 * a)
        print("Root 1 Is: ", root1)
        print("Root 2 Is: ", root2)    
    


        