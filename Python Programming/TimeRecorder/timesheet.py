# Program: timesheet.py
# This program is to calculate hours worked, overtime hours worked.

def weeklyPay(hoursWorked, wage):
    if hoursWorked >= 40:
        return 40 * wage + (hoursWorked - 40) * wage * 1.5
    else:
        return hoursWorked * wage
    
hoursWorked = float(input("How many hours did you work? >> "))
wage = float(input("What is your hourly rate? >> "))

pay = weeklyPay(hoursWorked,wage)

print(f"Total gross pay: {pay:.2f}")