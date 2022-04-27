# printfile.py
#   Prints a file to the screen

def main():
    fname = input("Enter file name: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)
main()