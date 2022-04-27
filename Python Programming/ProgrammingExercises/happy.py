# happy.py 
# This is a program that will sing happy birthday to the name the user inputs


def happy():
    print("Happy Birthday to you!")
    
def sing(person):
    happy()
    happy()
    print("Happy Birthday, dear", person + ".")
    
def main():
    sing("Joe")
    print()
    sing("Jane")
    print()
    sing("John")
main()