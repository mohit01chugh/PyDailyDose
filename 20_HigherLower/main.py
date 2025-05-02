logo='''         
        __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/       

    '''

vs = '''
     _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)    
            '''

game_data = [
    {
        "name": "Instagram",
        "follower_count": 460000000,
        "description": "Photo and video-sharing social networking service",
        "country": "United States"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 561000000,
        "description": "Portuguese professional footballer",
        "country": "Portugal"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 386000000,
        "description": "American actor, producer, and professional wrestler",
        "country": "United States"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 417000000,
        "description": "American singer, actress, and producer",
        "country": "United States"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 409000000,
        "description": "American media personality, model, and businesswoman",
        "country": "United States"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 459000000,
        "description": "Argentine professional footballer",
        "country": "Argentina"
    },
    {
        "name": "Neymar",
        "follower_count": 206000000,
        "description": "Brazilian professional footballer",
        "country": "Brazil"
    },
    {
        "name": "National Geographic",
        "follower_count": 226000000,
        "description": "American multinational nonprofit scientific and educational organization",
        "country": "United States"
    },
    {
        "name": "Real Madrid CF",
        "follower_count": 155000000,
        "description": "Spanish professional football club",
        "country": "Spain"
    },
    {
        "name": "Virat Kohli",
        "follower_count": 249000000,
        "description": "Indian cricketer",
        "country": "India"
    }
]


import random 
import os

def clear_screen():
    # Clear the console screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    print(logo)  # Display the game logo
    score = 0  # Initialize the player's score
    main = list(range(len(game_data)))  # Create a list of indices for game data
    
    continue_check = True
    while continue_check:
        # Randomly select two different entries from game data
        v1 = random.choice(main)
        v2 = random.choice(main)
        while v2 == v1:  # Ensure the second choice is different from the first
            v2 = random.choice(main)
                       
        # Display the two options for comparison
        print(f"Compare A: {game_data[v1]['follower_count']}, {game_data[v1]['description']}, from {game_data[v1]['country']}\n{vs}")
        print(f"Against B: {game_data[v2]['follower_count']}, {game_data[v2]['description']}, from {game_data[v2]['country']}")

        # Get user input to determine which option has more followers
        incomp = input("Who has more followers? Type 'A' or 'B': ")
        # Check if the user's guess is correct
        if (game_data[v1]["follower_count"] > game_data[v2]["follower_count"] and incomp.lower() == "a") or \
           (game_data[v1]["follower_count"] < game_data[v2]["follower_count"] and incomp.lower() == "b"):
            score += 1  # Increment score for a correct guess
            main.remove(v1)  # Remove the used entry from the list
            print(f"You're right! Current Score: {score}") 
        else:
            clear_screen()  # Clear the screen on a wrong guess
            print(f"Sorry, that's Wrong. Final Score: {score}") 
            continue_check = False  # End the game on a wrong guess
        
        # Check if there are fewer than 2 entries left to compare
        if len(main) < 2:
            print(f"Congrats, You are winner with Final Score {score}")
            break
                 
    # Ask the player if they want to play again
    while True:
        play_again = input("Do you want to play a game of HigherLower? Type 'y' or 'n': ").lower()
        if play_again == 'y':
            clear_screen()  # Clear screen for a new game
            play_game()  # Start a new game
        elif play_again == 'n':
            break  # Exit the game
        else:
            print("Invalid input. Please type 'y' or 'n'.")  # Handle invalid input

play_game()  # Start the game
