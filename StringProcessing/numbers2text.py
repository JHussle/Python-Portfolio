# numbers2text.py 
# A program that will convert a sequence of Unicode numbers into a string of text

def main():
    print("This is a program that will convert a sequence of Unicode numbers into a string of text")
    
    # Get message to encode 
    
    inString = input("Please enter the Unicode-encoded message: ")
    
    # Loop through each substring and build Unicode message
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr) # convert digits to a number
        message = message + chr(codeNum) # concatenate characters to message
        
    print("\nThe decoded message is:", message)
    
main()