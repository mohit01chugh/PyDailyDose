from turtle import Turtle, Screen

# Create a turtle and screen object
tim = Turtle()
screen = Screen()

# Function to clear the screen and reset turtle position
def clear_screen():
    tim.clear()  # Clear the drawing
    tim.penup()  # Lift the pen to avoid drawing while moving
    tim.home()   # Move turtle to the starting position
    tim.pendown()  # Put the pen down to draw again

# Function to move the turtle forward
def move_forwards():
    tim.forward(10)  # Move forward by 10 units

# Function to move the turtle backward
def move_backward():
    tim.backward(10)  # Move backward by 10 units

# Function to turn the turtle left
def turn_left():
    tim.setheading(tim.heading() + 10)  # Turn left by 10 degrees

# Function to turn the turtle right
def turn_right():
    tim.setheading(tim.heading() - 10)  # Turn right by 10 degrees

# Set up key listeners for turtle movement
screen.listen()  # Start listening for key presses
screen.onkey(key="w", fun=move_forwards)  # Move forward on 'w' key press
screen.onkey(key="s", fun=move_backward)  # Move backward on 's' key press
screen.onkey(key="a", fun=turn_left)      # Turn left on 'a' key press
screen.onkey(key="d", fun=turn_right)     # Turn right on 'd' key press
screen.onkey(key="c", fun=clear_screen)   # Clear screen on 'c' key press

# Wait for a click to exit the program
screen.exitonclick()
