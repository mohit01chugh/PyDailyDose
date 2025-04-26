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

print("Welcome to the secret auction program")  # Welcome message
dicy = {}  # Dictionary to store bidder names and their bids

def clear_screen():
    # Clear the console screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def bid():
    # Function to collect bid information from a bidder
    in1 = input("What is your name:\n")  # Get bidder's name
    in2 = int(input("What is your bid:\n$"))  # Get bidder's bid amount
    dicy[in1] = in2  # Store the name and bid in the dictionary
    
bid()  # Call the bid function for the first bidder

continue_check = True  # Flag to control the bidding loop
while continue_check:
    in3 = input("Are there any other bidders? Type 'yes' or 'no'.\n")  # Ask if there are more bidders
    if in3 == "yes":
        clear_screen()  # Clear the screen for the next bidder
        bid()  # Call the bid function for the next bidder
    elif in3 == "no":
        continue_check = False  # Exit the loop if no more bidders
        highest = max(dicy.values())  # Find the highest bid
        for name, values in dicy.items():  # Iterate through the bids
            if values == highest:  # Check for the winner(s)
                print(f"The winner is {name} with a bid of ${highest}")  # Announce the winner
    else:
        print("Please enter a valid input")  # Prompt for valid input if the response is invalid