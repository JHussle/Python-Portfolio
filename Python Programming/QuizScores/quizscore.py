# quizscore.py
#   This program will grade a test on an scale of 5-1.
#     when the user enters 5-A, 4-B, 3-C, 2-D, 1-F

def main():
    
    # User input for the points earned
    score = int(input("Enter score from quiz (1-5): "))
    
    # Grading score list
    if score == 5:
        print("A")
    elif score == 4:
        print("B")
    elif score == 3:
        print("C")
    elif score == 2:
        print("D")
    elif score == 1:
        print("F")
    else:
        print("F")
        

        
main()
    
    