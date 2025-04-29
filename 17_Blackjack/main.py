# ASCII art for Blackjack
Blackjack = '''
                .------.            _     _            _    _            _    
                |A_  _ |.          | |   | |          | |  (_)          | |   
                |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
                | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
                |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
                '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
                    |  \/ K|                            _/ |                
                    '------'                           |__/           
'''

import os
import random

def clear_screen():
    # Clear the console screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def deal():
    # Return a random card value (1-11 for Ace, 2-10 for numbered cards, 10 for face cards)
    card = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])  # Face cards are worth 10
    return card

def compare(your_score, comp_score):
    # Compare scores and determine the outcome of the game
    if your_score == comp_score:
        return "*************************Draw*************************"
    elif comp_score == 0:
        return "************Lose, opponent has Blackjack*************"
    elif your_score == 0:
        return "***************Win with a Blackjack******************"
    elif your_score > 21:
        return "**************You went over. You Lose*****************"
    elif comp_score > 21:
        return "***********Opponent went over. You win***************"
    elif your_score > comp_score:
        return "**********************You win************************"
    else:
        return "**********************You Lose************************"

def sumt(cards):
    # Calculate the total score of the cards, considering Blackjack and Ace value
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 1 in cards and sum(cards) + 10 <= 21:  # Consider Ace as 11 if it doesn't bust
        return sum(cards) + 10
    return sum(cards)

def play_game():
    print("Welcome to Blackjack!")  # Game introduction
    your_card = []  # Player's cards
    comp_card = []  # Computer's cards
    
    # Deal initial cards
    for _ in range(2):
        your_card.append(deal())
    comp_card.append(deal())

    continue_card = True
    while continue_card:
        your_score = sumt(your_card)  # Calculate player's score
        comp_score = sumt(comp_card)  # Calculate computer's score
        print(f"Your Cards: {your_card}, Current score: {your_score}\nComputer's first card: {comp_card}")

        # Check for game-ending conditions
        if your_score == 0 or comp_score == 0 or your_score > 21:
            continue_card = False 
        else:
            your_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if your_choice.lower() == "y":
                your_card.append(deal())  # Player chooses to take another card
            else:
                continue_card = False

    # Dealer's turn to draw cards
    while comp_score != 0 and comp_score < 17:
        comp_card.append(deal())
        comp_score = sumt(comp_card)

    # Display final hands and scores
    print(f"Your final hand: {your_card}, final score: {your_score}\nComputer's final hand: {comp_card}, final score: {comp_score}")
    print(compare(your_score, comp_score))  # Compare scores and determine the winner

    # Ask if the player wants to play again
    while True:
        play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play_again == 'y':
            clear_screen()  # Clear screen for a new game
            play_game()  # Start a new game
        elif play_again == 'n':
            break  # Exit the game
        else:
            print("Invalid input. Please type 'y' or 'n'.")

play_game()  # Start the game