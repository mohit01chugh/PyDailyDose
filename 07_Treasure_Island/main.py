import sys  # Import the sys module for system-specific parameters and functions

# Print the introductory ASCII art and welcome message
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

print("You are at a crossroad. Where do you want to go?\n")

# Prompt user to choose a direction
go1 = input('''Type "left" or "right"\n''').lower()
if (go1 == "right"):  # Check if the user chose the right path
    print("Fall into a hole.\nGame Over.")  # End game if right is chosen
    sys.exit()  # Exit the program
else:
    print("You have come to a lake. There is an island in the middle of the lake.")

# Prompt user to choose an action at the lake
go2 = input('''Type "wait" to wait for a boat. Type "swim" to swim across.\n''').lower()
if go2 == "swim":  # Check if the user chose to swim
    print("Attacked by trout.\nGame Over.")  # End game if swimming is chosen
else:
    print("text")  # Placeholder for waiting action

# Prompt user to choose a door
go3 = input('Which door "red" or "blue" or "yellow"\n.').lower()
if (go3 == "yellow"):  # Check if the user chose the yellow door
    print("You Win!")  # Player wins if yellow is chosen
elif (go3 == "red"):  # Check if the user chose the red door
    print("Burned by fire.\nGame Over.")  # End game if red is chosen
elif (go3 == "blue"):  # Check if the user chose the blue door
    print("Eaten by beasts.\nGame Over.")  # End game if blue is chosen
else:
    print("You typed the wrong input")  # Handle invalid input