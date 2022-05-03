# quizscore2.py
# A program that the user will be able to enter a score and get the grade printed to themselves


def gradebook(score):
    if score >= 90:
        return 'A'
    elif score < 90 and score >= 80:
        return 'B'
    elif score < 80 and score >= 70:
        return 'C'
    elif score < 70 and score >= 60:
        return 'D'
    else:
        return 'F'

score = int(input("Please enter quiz score. >> "))

grade = gradebook(score)

print("Quiz grade is: ", grade)