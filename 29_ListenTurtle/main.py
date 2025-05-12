from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Define movement function triggered by space key
def move():
    tim.forward(100)  # Move forward 100 units
    tim.left(90)      # Turn left 90 degrees
    tim.backward(100) # Move backward 100 units
    tim.right(90)     # Turn right 90 degrees

screen.listen()  # Start listening for key presses
screen.onkey(key="space", fun=move)  # Bind space key to move function

screen.exitonclick()  # Wait for mouse click to exit
