# convert.py
#   A program to convert Celsius to Fahrenheit
# Joey Smith

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = (9/5 * celsius) + 32
    print("The temperature is", fahrenheit, " degrees Fahrenheit.")

    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (5/9 * fahrenheit) - 32
    print("The temperature is", celsius, " degrees Celsius.")

main()