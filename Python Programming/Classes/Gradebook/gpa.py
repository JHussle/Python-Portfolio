# gpa.py
# Program to find student with highest GPA

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    
    def getName(self):
        return self.name
    
    def getHours(self):
        return self.hours
    
    def getQpoints(self):
        return self.qpoints
    
    def gpa(self):
        return self.qpoints/self.hours
    
    def makeStudent(infoStr):
        #infoStr is a tab-seperated line: name hours qpoints
        # returns a corresponding Student object
        name, hours, qpoints = infoStr.split("\t")
        return Student(name, hours, qpoints)
    
    def main():
        #ope the input file for reading
        filename = input("Enter the name of the grade file: ")
        infile = open(filename, 'r')
        
        # set best to the recored for the first student in the files
        best = makeStudent(infile.readline)
        
        # process subsequent lines of the file
        for line in infile:
            # turn the line into s student recored
            s = makeStudent(line)
            # if this student is best so far, remember it.
            if s.gpa() > best.gpa():
                best = s
                infile.close()
    if __name__ == "__main__":
        main()