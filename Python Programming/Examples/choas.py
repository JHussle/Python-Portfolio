def main():
    print("This program illustrates a chaotic funcation")
    x = eval(input("Enter a number between 0 and 1:"))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)
    y = eval(input("Enter a number between 0 and 1:"))
    for i in range(10):
        y = 2.0 * y * (1 - x)
        print(y)   
main()