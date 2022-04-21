# molecular.py 
########################################################################
# This program computes the molecular weight of a molecular       
# weight of a carbohydrate (in grames per mole). Bases on the     
# number of hydrogen, carbon, and oxygen atoms in the molecule.   
# This program should prompt the user to enter the number of hydrogen
# atom, the number of carbon atoms, and the number of oxygen atoms.
# This program then prints the total combined molecular weight of all
# the attoms bases on the individual atoms weights.
#
########################################################################


import math

def main():
    
    h = float(input("Please enter molecule weight hydrogen: "))
    c = float(input("Please enter molecule weight carbon: "))
    o = float(input("Please enter molecule weight oxygen: "))
    
    hydrogen = 1.007942
    carbon = 12.0107
    oxygen = 15.9994
    
    result = (h * hydrogen) + (c * carbon)  + (o * oxygen)
    
    print("The molecular weight is: ", result)
    
    
main()