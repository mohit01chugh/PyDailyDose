hang0 = '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''

hang1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
'''

hang2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''

hang3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''

hang4 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
hang5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
hang6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''

banner = print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')

hang = [hang0,hang1,hang2,hang3,hang4,hang5,hang6]

import random
import sys
from PyDictionary import PyDictionary
import nltk
from nltk.corpus import words

# Download NLTK words corpus
nltk.download('words')
word_list = words.words()  # List of words for the game
random_word = random.choice(word_list)  # Randomly select a word

# Get the meaning of the random word
dictionary = PyDictionary()
meaning = dictionary.meaning(random_word)

# Create a placeholder for the word to guess
placeholder = "_" * len(random_word)
print(f"Word to guess: {placeholder}")

# Function to provide a hint
def hint():
    inhint = input("Do you want any hint? Y or N: \n").lower()
    if inhint == "y":
        print(meaning)  # Print the meaning of the word
    else:
        print("Best of Luck! Try yourself")

# Function to provide additional help
def add_help():
    helpig_word = list(random_word)  # Convert the random word to a list
    inhelp = input("Do you need additional help? Y or N: \n").lower()
    if inhelp == "y":
        # Show every second letter as a hint
        for position in range(len(random_word)):
            if position % 2 != 0:
                helpig_word[position] = "_"
        print("".join(helpig_word))  # Print the modified word
        print("For Save the live")   
    else:
        print("Best of Luck !!!")

# Game initialization
Game_Over = False
correct_letter = []  # List to track correct guesses
lives = 0  # Number of lives

# Main game loop
while not Game_Over:
    ing = input("Guess a letter: ").lower()  # User input for letter guess
    display = ""
    
    # Build the display string based on guesses
    for letter in random_word:
        if ing == letter:
            display += letter
            correct_letter.append(ing)  # Add correct guess to the list
            print(f"****************************{6-lives}/6 LIVES LEFT****************************")
        elif letter in correct_letter:
            display += letter  # Show correctly guessed letters        
        else:
            display += "_"  # Show placeholder for unguessed letters
    
    print(display)  # Show current state of the word
    
    # Check if the guessed letter is in the word
    if ing not in random_word:
        print(f" You guessed {ing}, that's not in the word. You lose a life.\n{hang[lives]}")
        print(f"****************************{5-lives}/6 LIVES LEFT****************************")    
        lives += 1  # Increment lives lost
        
        # Provide hints or help based on lives left
        if lives == 4:
            hint()
        elif lives == 5:
            add_help()
        elif lives == 6:
            print(f" You guessed {ing}, that's not in the word. You lose a life.\n{hang[6]}")
            print(f"***********************IT WAS {random_word}! YOU LOSE**********************")
            sys.exit()  # End the game

    # Check if the player has won
    if "_" not in display:
        Game_Over = True
        print("****************************You Win****************************")