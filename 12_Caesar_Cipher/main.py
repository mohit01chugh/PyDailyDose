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
alphabet = list(string.ascii_lowercase)

def positions(num):
        indexing = []
        for char in msg:
            if char in alphabet:
                indexi = alphabet.index(char) + num
                if indexi > 25:
                     indexi = indexi - len(alphabet)
                indexing.append(indexi)   
            elif char == " ":
                space = "+"
                indexing.append(space)

        actual = []
        for value in range(len(indexing)):
             new = indexing[value]
             if new is "+":
                  actual.append("+")
             else:
                  new_inv = int(new)
                  actext = alphabet[new_inv]
                  actual.append(actext)

        joining = "".join(actual)
        fjoin = joining.replace("+"," ")

        if task == "0":
             print(f"Here's the Encoded result:{fjoin}")
        else:
             print(f"Here's the Decoded result:{fjoin}")

continue_check = True

while continue_check:

          task = int(input('''Type '0' for "encode" to encrypt, type '1' for "decode" to decrypt:\n'''))
          if task > 1:
               print("Please Enter the Vaild Input")
               sys.exit()

          in_msg = input("Type your message:\n")
          shift = int(input("Type the shift number:\n"))
          msg = list(in_msg)
          
          if (task == 0):
               positions(shift)
          else:
               minus_shift = - shift
               positions(minus_shift)
               
          restart = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n")
          if restart == "no":
               continue_check = False
               print("Good Bye for now!!!")
               sys.exit()
          
          



     

