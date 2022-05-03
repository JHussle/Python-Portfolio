# quizscore2.py
# A program that the user will be able to enter a score and get the grade printed to themselves


def gradebook(score):
    if score == 5:
        return 'A'
    elif score == 4:
        return 'B'
    elif score == 3:
        return 'C'
    elif score == 2:
        return 'D'
    else:
        return 'F'

score = int(input("Please enter quiz score. >> "))

grade = gradebook(score)

print("Quiz grade is: ", grade)