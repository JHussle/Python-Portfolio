# examscore.py
#   This program will grade a test on an grading scale of 1-100.
#     when the user enters 90 < A, 80 < = 89 B, 70 <= 79 C, 60 <= 69 D, 59 > F


def main():
    
    a = "A"
    b = "B"
    c = "C"
    d = "D"
    f = "F"
    
    # exam logic
    score = float(input("Enter exam score: "))
    
    if score >= 90 and score <= 100:
        print("Your exam score is: ", score, "and your grade is:", a)
    elif score >= 80 and score <= 89:
        print("Your exam score is: ", score, "and your grade is:", b)
    elif score >= 70 and score <= 79:
        print("Your exam score is: ", score, "and your grade is:", c)
    elif score >= 60 and score <= 69:
        print("Your exam score is: ", score, "and your grade is:", d)
    elif score >= 59:
        print("Your exam score is: ", score, "and your grade is:", f)
    else:
        print("No Marks")
main()