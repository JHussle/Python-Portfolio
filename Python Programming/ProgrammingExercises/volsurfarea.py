# volsurfarea.py
# # FIrst exercise.
# This program will calculate the volume and the surface area
# of a sphere from its radius, given as points.

from locale import ABDAY_5
import math

def main():
    
    print("This program will calculate the volume and the surface area.")
    print("of a sphere from its radius, given as points.")
    
    r = float(input("Enter the radius: "))
    # a = float(input("Enter the surface area: "))
    pi = 3.141592653589793
    
    volume = 4/3 * pi * r ** 3
    surfacearea = 4 * pi * r * r 
    
    
    print("The volume and surface area: ", volume, surfacearea)
    # print("The surface area is: ", area)
    
main()