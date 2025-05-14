from turtle import Turtle, Screen
from random import randint

# Set up the screen dimensions
screen = Screen()
screen.setup(500, 400)

# List of turtle colors
color = ["red", "orange", "blue", "green", "yellow", "purple"]
# Prompt user for their bet on which turtle will win
user_bet = screen.textinput("Make your bet", "Which Turtle Win?")
# Y-coordinates for turtle starting positions
ypost = [-70, -40, -10, 20, 50, 80]

# Create a list to hold all turtle objects
all_turtle = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")  # Create a new turtle
    new_turtle.color(color[i])            # Set turtle color
    new_turtle.penup()                    # Lift pen to avoid drawing
    new_turtle.goto(x=-230, y=ypost[i])   # Position turtle at starting line
    all_turtle.append(new_turtle)         # Add turtle to the list

# Flag to control the race loop
is_race_on = True

# Main race loop
while is_race_on:
    for check in all_turtle:
        if check.xcor() > 230:  # Check if turtle has crossed the finish line
            is_race_on = False  # End the race
            winning_color = check.pencolor()  # Get the winning turtle's color
            # Determine if the user won or lost
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

        random_distance = randint(0, 10)  # Generate a random distance for the turtle to move
        check.forward(random_distance)      # Move the turtle forward

# Wait for a click to exit the program
screen.exitonclick()
