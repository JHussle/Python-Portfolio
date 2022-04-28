# calculator.py
#
# This program is a calculator the first option
# the user will be able to do basic calculations
# upto 100.
# This calculator will have other functions at a later
# time.

def main():
    print("Welcome to the Calculator Program.")
    print("In this Calculator you will be able to perform basic calculations.")
    print("Addition, Subtraction, Division, and Multiplication")
    
    for x in range(10): 
        x = eval(input("Please input what you want calculated: "))
    
        
        result = x
        
        print(result)
    
main()