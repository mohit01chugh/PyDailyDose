print('''        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88               
      ''')

import string
import sys

# Create a list of lowercase alphabet letters
alphabet = list(string.ascii_lowercase)

def positions(num):
    indexing = []  # List to hold the shifted positions of characters
    for char in msg:
        if char in alphabet:  # Check if the character is a letter
            indexi = alphabet.index(char) + num  # Shift the index by num
            if indexi > 25:  # Wrap around if index exceeds alphabet length
                indexi = indexi - len(alphabet)
            indexing.append(indexi)   
        elif char == " ":  # Handle spaces
            space = "+"
            indexing.append(space)

    actual = []  # List to hold the final characters
    for value in range(len(indexing)):
        new = indexing[value]
        if new is "+":  # Check for space placeholder
            actual.append("+")
        else:
            new_inv = int(new)  # Convert index back to character
            actext = alphabet[new_inv]
            actual.append(actext)

    joining = "".join(actual)  # Join the characters into a string
    fjoin = joining.replace("+", " ")  # Replace placeholder with spaces

    # Print the encoded or decoded result based on the task
    if task == "0":
        print(f"Here's the Encoded result: {fjoin}")
    else:
        print(f"Here's the Decoded result: {fjoin}")

continue_check = True  # Control variable for the main loop

while continue_check:
    # Prompt user for task selection
    task = int(input('''Type '0' for "encode" to encrypt, type '1' for "decode" to decrypt:\n'''))
    if task > 1:  # Validate input
        print("Please Enter the Valid Input")
        sys.exit()

    in_msg = input("Type your message:\n")  # Get the message from user
    shift = int(input("Type the shift number:\n"))  # Get the shift value
    msg = list(in_msg)  # Convert message to a list of characters
    
    # Call positions function with appropriate shift
    if (task == 0):
        positions(shift)  # Encode
    else:
        minus_shift = -shift  # Decode by negating the shift
        positions(minus_shift)
        
    # Ask user if they want to continue
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n")
    if restart == "no":
        continue_check = False  # Exit loop if user chooses not to continue
        print("Good Bye for now!!!")
        sys.exit()
          
          



     

