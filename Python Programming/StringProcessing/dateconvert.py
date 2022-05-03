# dateconvert.py --
# Convert a date in form "mm/dd/yyyy" to "month, day, year"

def main():
    
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")
    
    # split into components
    monthSrt, dayStr, yearStr = dateStr.split("/")
    
    # convert monthStr to the month name
    
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]
    
    monthSrt = months[int(monthSrt) - 1]
    
    # output result in month day, year format
    print("The convert date is: ", monthSrt, dayStr+ ",", yearStr)
    
main()