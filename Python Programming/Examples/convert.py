# convert.py
#   A program to convert Celsius to Fahrenheit
# Joey Smith


def main():
    
    print("This program convert temperature")
    print("currently the conversion is from fahrenheit to celsius.")
    
    celsius = eval(input("What is the Celsius temperature? "))    
    fahrenheit = (9/5 * celsius) + 32
    print("The temperature is", fahrenheit, " degrees Fahrenheit.")

    if fahrenheit > 90:
        print("Heat warning is in effect")
        
    if fahrenheit > 30:
        print("Cold warning is in effect")


main()