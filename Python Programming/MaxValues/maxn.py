# program: maxn.py
#   Finds the maxium of the series of numbers

def main():
    n = int(input("How many numbers are there? "))
    
    # Set max to be the first value
    maxval = float(input("Enter a number >> "))
    
    # Now compare the n-1 successive values
    for i in range(n-1):
        x = float(input("Enter a number >> "))
        if x > maxval:
            maxval = x
            
        print("The largest value is", maxval)
main()