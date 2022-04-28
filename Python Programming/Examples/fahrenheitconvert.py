# A program that will convert from Fahrenheit to Celsius


def main():
    
    print("This program convert temperature")
    print("currently the conversion is from fahrenheit to celsius.")
    
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    
    for fahrenheit in range(0, 101, 10):
            
        celsius = (5/9 * fahrenheit) - 32
        print("The temperature is", celsius, " degrees Celsius.")

main()