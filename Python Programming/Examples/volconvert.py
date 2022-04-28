# volconvert.py
#
# This program will convert liters into gallons

def main():
    
    print("This program convert liquid measurements")
    print("currently the conversion is from Liters to Gallons.")
    
    liters = eval(input("How many liters do you have?: "))        
    gallons = liters * 0.264172
    print("The conversion that you have is", gallons, " gallons.")

main()