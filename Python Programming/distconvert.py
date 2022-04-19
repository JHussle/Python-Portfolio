# This is a program that will convert distance.
# kilometers to miles 


def main():
    
    print("This program convert distance")
    print("currently the conversion is from kilometers to miles.")
    
    kilometers = eval(input("Please enter the kilometers to be converted: "))
    
    miles = kilometers / 0.6214
    print("Kilometers to miles is: ", miles)
    
main()