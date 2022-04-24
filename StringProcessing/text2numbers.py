#text2numbers.py
# A program that will convert a textual message into a sequence of
#   numbers, utilizing the underlying Unicode encoding.

def main():
    print("This program will convert a textual message into a sequence of")
    print("numbers representing the Unicode encoding of the message.")
    
    # Get the message to encode
    message = input("Please enter the message to encode: ")
    
    print("\nHere are the Unicode code: ")
    
    # Loop through the message and print the Unicode values
    
    for ch in message:
        print(ord(ch), end=" ")
        
    print() # blank line before prompt
    
main()