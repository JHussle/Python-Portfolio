# collegecredits.py
# A program that will tell you what the students status is by the amount of credits.
#   if a student has 7 crdit or less they are a freshman, 7 or more a sophmore, 16 to be a junior
#       26 or more to be a senior 26

def transcript(credits):
    if credits < 7:
        return 'Freshman'
    elif credits >= 7 and credits < 16:
        return 'Sophmore'
    elif credits >= 16 and credits < 26:
        return 'Junior'
    else:
        return 'Senior'
    
credits = int(input("Please enter college credit. >> "))
studentStatus = transcript(credits)

print("Your student status is: ", studentStatus)

