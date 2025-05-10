from turtle import Turtle, Screen
from random import randint, choice

# Create a turtle and screen object
tim = Turtle()
screen = Screen()
screen.colormode(255)  # Set color mode to RGB

# Define possible movement directions
direction = [0, 90, 180, 270]

# Function to generate a random color
def colors():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

# Draw 100 lines with random colors and directions
for _ in range(100):
    tim.width(5)  # Set the pen width
    tim.color(colors())  # Set a random color
    tim.speed("fastest")  # Set the turtle speed to fastest
    tim.forward(25)  # Move the turtle forward by 25 units
    tim.setheading(choice(direction))  # Change direction randomly

# Wait for a click to exit
screen.exitonclick()
