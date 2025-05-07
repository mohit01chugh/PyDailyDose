from turtle import Turtle, Screen

# Create a turtle and screen object
tim = Turtle()
screen = Screen()

# Draw a square
for _ in range(4):
    tim.forward(100)  # Move forward 100 units
    tim.left(90)      # Turn left 90 degrees

# Wait for a click to exit
screen.exitonclick()
