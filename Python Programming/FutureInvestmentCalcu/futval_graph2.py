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


from graphics import *

def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")
    
    #Get principal and interest rate
    principal = float(input("Enter the inital principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    
    # Create a graphics window with labels on the left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0k').draw(win)
    Text(Point(-1, 2500), ' 2.5k').draw(win)
    Text(Point(-1, 5000), ' 5.0k').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), ' 10.0k').draw(win)
    
    # Draw bar for initial principal
   
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    
    # Draw bars for successive years
    for year in range(1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        
    input("Press <Enter> to quit")
    win.close()
    
main()






























