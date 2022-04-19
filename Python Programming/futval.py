# futval.py
#   A program to compute the value of an investment
#   carried 10 years into the future

def main():
    print("This program calculate the future value")
    print("of a X number of years investment.")
    
    principal = eval(input("Enter the inital principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    yrs = eval(input("Enter the number of years for investment: "))
    
    for i in range(1, 2, 3, 4, 5):
        principal = principal * (1 + apr)
    
    convert_num = str(yrs)    
    print("The value in " + convert_num + " is:", principal)
main()