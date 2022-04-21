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
    Text(Point(20, 230), ' 0.0k').draw(win)
    Text(Point(20, 180), ' 2.5k').draw(win)
    Text(Point(20, 130), ' 5.0k').draw(win)
    Text(Point(20, 80), ' 7.5k').draw(win)
    Text(Point(20, 30), ' 10.0k').draw(win)
    
    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    
    # Draw bars for successive years
    for year in range(1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        
        # draw bar for this values
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11+25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        
    input("Press <Enter> to quit")
    win.close()
    
main()






























