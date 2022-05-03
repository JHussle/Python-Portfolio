# futval_graph.py
from graphics import *

def drawBar(window, year, height):
    # Draw a bar in window starting at year with given height
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("yellow")
    bar.setWidth(2)
    bar.draw(window)

# Returns a GraphWin wiht titile and labels drawn
def createLabledWindow():
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), '0.0k').draw(window)
    Text(Point(-1, 2500), '2.5k').draw(window)
    Text(Point(-1, 5000), '5.0k').draw(window)
    Text(Point(-1, 7500), '7.5k').draw(window)
    Text(Point(-1, 10000), '10.0k').draw(window)
    return window
    
def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")
    
    # Get principal and interest rate
    principal = float(input("Enter the inital principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    
    win = createLabledWindow()
    drawBar(win, 0, principal)
    for year in range(1, 11):
        principal = principal * (1 + apr)
        drawBar(win, year, principal)
        
    input("Press <Enter> to quit.")
    win.close()
main()