# average5.py

def main():
    fileName = input("What file are the number in? ")
    infile = open(fileName, "r")
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        total = total + float(line)
        count = count + 1
    print("\nThe average of the numbers is", total / count)
main()