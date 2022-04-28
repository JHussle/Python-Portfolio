# futval.py
#   A program to compute the value of an investment
#   carried XX years into the future

############################################################################
#
# Print an introduction
# Get value of principal and apr from user
# Create a 320x240 GraphWin Titled "Investment Growth Chart"
#   -- Draw label " 0.0k" at (20,230)
#   -- Draw label " 2.5k" at (20,180) 
#   -- Draw label " 5.0k" at (20,130)
#   -- Draw label " 7.5k" at (20,80)
#   -- Draw label " 10.0k" at (20,30)
#  Draw a rectangle from (40, 230) to (65,230 - principal * 0.02)
# 
# Create a GraphWin
# Draw bar at the position 0 with height corresponding to principal
# For successive yearr 1 through 10 years
#       -- Calculate principal = principal * (1 + apr)
#       -- Draw a bar for this year having height corresponding to principal
# 
# Wait for user to press enter
#
########################################################################
# 
# For year running form a value of 1 up through 10:
#   -- Calculate principal = principal * (1 + apr)
#   -- Calculate x11 = 25 * year + 40
#   -- Calclate height = principal * 0.02
#   -- Draw a rectangle from (x11, 230) to (x11+25, 230 - height)
# 
###########################################################################
#
# 
# 
# 
# 
# 
# 
# 
###########################################################################

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