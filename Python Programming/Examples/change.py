# change.py 
# A program to calculate the value of some change in dollars.

from shelve import DbfilenameShelf


def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print()
    print("The total value of your change is ${0:0.2f}".format(total))

main()