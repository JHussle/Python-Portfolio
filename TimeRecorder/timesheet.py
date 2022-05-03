# Program: timesheet.py
# This program is to calculate hours worked, overtime hours worked.

def main():
    payRate = float(input("Please enter pay rate: "))
    hours = float(input("How many hours worked this week? "))
    
    if hours >= 40