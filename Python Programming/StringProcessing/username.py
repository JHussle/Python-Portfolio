# username.py
#   Simple string processing program to generate username. This

def main():
    print("This program generate computer username. \n")
    
    # get user's first and last namespace
    
    first = input("Please enter your first name (all lower case): ")
    last = input("Please enter your last name (all lower case): ")
    
    # concatenate the first initial with 7 char of the last name.
    
    uname = first[0] + last[:7]
    
    # output of username 
    
    print("Your username is:", uname)

main()