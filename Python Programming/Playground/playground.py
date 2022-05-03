def main():
    x1, x2, x3, x4 = eval(input("Please enter three values: "))
    
    if x1 >= x2:
        if x1 >= x3:
            if x1 >= x4:
                maxval = x1
            else:
                maxval = x4
        else:
            maxval = x3
    else:
        if x2 >= x3:
            maxval = x2
            if x2 >= x4:
                maxval = x2
            else:
                maxval = x4
        print("The largest value is", maxval)
main()
