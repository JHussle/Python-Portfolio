#numbers2text.py 
#   A program tp convert a sequence of Unicode numbers into
#       a string of text. Efficient version using a list accumlator.

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that is represents.\n")
    
    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")
    
    # Loop through each substring and build Unicode message
    char = []
    for numStr in inString.split():
        codeNum = int(numStr)   # convert digits to number
        char.append(chr(codeNum))   # accumulate new character
        
    message = "".join(char)
    print("\nThe decoded message is:", message)
    
main()