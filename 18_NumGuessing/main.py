logo = '''
          / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|      
                                                                                                '''

import random
import sys

# Print the game logo and welcome message
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

def compare():
    # Compare the guessed number with the random number
    if (rdnum > num):
        print("Too Low\nGuess again.")  # Guess is too low
    elif (rdnum < num):
        print("Too High\nGuess again.")  # Guess is too high
    else: 
        print(f"You got it! The answer was {num}")  # Correct guess
        sys.exit()  # Exit the game

# Generate a random number between 1 and 100
rdnum = random.randint(1, 100)
task = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Set the number of attempts based on difficulty level
if task == "easy":
    for i in range(10):  # 10 attempts for easy mode
        print(f"You have '{10 - i}' attempts remaining to guess the number.")
        num = int(input("Make a guess: "))  # Get user guess
        compare()  # Compare guess with the random number
        if i == 9:
            print("You've run out of guesses. Refresh the page to run again.")  # Out of attempts
elif task == "hard":
    for i in range(5):  # 5 attempts for hard mode
        print(f"You have '{5 - i}' attempts remaining to guess the number.")
        num = int(input("Make a guess: "))  # Get user guess
        compare()  # Compare guess with the random number
        if i == 4:
            print("You've run out of guesses. Refresh the page to run again.")  # Out of attempts
else:
    print("Please Enter the Valid Input")  # Invalid difficulty input