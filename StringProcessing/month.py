# month.py
# A program to print the abbreviation of a month, given its number.

def main():
    
    # months is used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    
    n = int(input("Enter a month number (1-12): "))
    
    # compute starting position of the month n in months
    pos = (n - 1) * 3
    
    # Grab the appropriate slice of the months
    monAbbrev = months[pos:pos+3]
    
    # print the results
    print("The month abbreviation is", monAbbrev + " .")
    
main()