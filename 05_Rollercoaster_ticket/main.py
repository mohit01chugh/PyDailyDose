import sys

# Welcome message for the roller-coaster
print("Welcome to the Roller-Coaster!")

# Get user's height in cm
height = int(input("What is your height in cm? \n"))

# Check if the user is tall enough to ride
if height >= 120:
    print("You can ride the rollercoaster")
    
    # Get user's age
    age = int(input("What is your age?\n"))
    
    # Determine ticket price based on age
    if age <= 12:
        ticket = 5
        print("Child tickets are $5")
    elif age <= 18:
        ticket = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        ticket = 0
        print("Everything is going to be ok. Have a free ride on us!")
        sys.exit()  # Exit if the user qualifies for a free ride
    else:
        ticket = 12
        print("Adult tickets are $12")

    # Ask if the user wants a photo taken
    wants_pic = input("Do you want to have a photo taken?\nType y for Yes or n for No\n")
    
    # Calculate final bill based on photo choice
    if wants_pic == "y":
        bill = ticket + 3  # Add photo cost
        print(f"Your Final bill is ${bill}")
    else:
        print(f"Your Final bill is ${ticket}")

else:
    print("Sorry you have to grow taller before you can ride")  # Message for insufficient height