import random
import sys

# Get user's choice
user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# Generate computer's choice
computer_choice = random.randint(0, 2)

# ASCII art representations of Rock, Paper, and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)          
          '''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)       
          '''

scissor = '''
     ______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)   
          '''

# List of images for easy access
img = [rock, paper, scissor]

# Check for invalid input
if (user_choice >= 3 or user_choice < 0):
    print(f"You typed an invalid number: {user_choice}, You lose!") 
    sys.exit()  # Exit the program for invalid input

# Determine the outcome of the game
elif (user_choice == 0 and computer_choice == 2):
    print(f"{img[user_choice]} \n Computer Choose: {computer_choice} {img[computer_choice]} \n You Win!")
elif (user_choice == 2 and computer_choice == 0):
    print(f"{img[user_choice]} \n Computer Choose: {computer_choice} {img[computer_choice]} \n You Lose!")
elif (computer_choice > user_choice):
    print(f"{img[user_choice]} \n Computer Choose: {computer_choice} {img[computer_choice]} \n You Lose!")
elif (user_choice > computer_choice):
    print(f"{img[user_choice]} \n Computer Choose: {computer_choice} {img[computer_choice]} \n You Win!")
else: 
    print(f"{img[user_choice]} \n Computer Choose: {computer_choice} {img[computer_choice]} \n It's a draw!")