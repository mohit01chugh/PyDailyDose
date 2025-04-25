print('''       
                          __________
                          \        /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'.------------'
                          )"""""""(
                         |_________|
                       .-------------.
                      |_______________|
                                            ''')

import os

print("Welcome to the secret acution program")
dicy = {}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bid():
    in1 = input("What your name:\n")
    in2 = int(input("What is your bid:\n$"))
    dicy[in1] = in2
    
bid()

continue_check = True
while continue_check:
    in3 = input("Are there any other bidder? Type 'yes or no'.\n")
    if(in3 == "yes"):
        clear_screen()
        bid()
    elif(in3 == "no"):
         continue_check = False
         highest = max(dicy.values())
         for name, values in dicy.items():
            if values == highest:
                print(f"The winner is {name} with a bid of {highest} ")
    else:
        print("Please Enter the Vaild input")
    