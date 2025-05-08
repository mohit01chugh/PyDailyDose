from turtle import Turtle, Screen

# Create a turtle and screen object
tim = Turtle()
screen = Screen()

# Draw a dashed line with 30 dashes
for _ in range(30):
    tim.forward(5)   # Draw forward 5 units
    tim.penup()      # Lift pen to stop drawing
    tim.forward(5)   # Move forward 5 units without drawing
    tim.pendown()    # Put pen down to resume drawing

# Wait for a click to exit
screen.exitonclick()
