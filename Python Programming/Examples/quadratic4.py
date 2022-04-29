# quadtric.py 
# A program that computes the real roots of a quadtric equation.
# Illustrates use of the math library
# Note: This program crashes if the equation has no real roots

import math # Makes the math library available

def main():
    print("This program finds the real solutions to quadtric equation")
    print()
    
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\nThe equation has no real root!")
    
    elif discrim == 0:
        root = -b / (2 * a)
        print("\nThere is a double root at", root)

    else: 
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        
        print("\nThe solutions are: ", root1, root2)
    

main()