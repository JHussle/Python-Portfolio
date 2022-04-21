# costpersq.py 
# This program calculate the cost per square inch of a circular pizza
# given its diameter and price.

import math

def main():
    
    print("This program calculate the cost per square inch of a circular pizza")
    print("given its diameter and price.")
    
    r = int(input("Enter the radius of the circular pizza: "))
    pi = 3.141592653589793
    
    
    area = pi * r ** 2
    
    print("The area is: ", area)
    
main()