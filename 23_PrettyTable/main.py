from turtle import Turtle, Screen

# Create a Turtle object named 'timmy'
timmy = Turtle()

# Print the Turtle object
print(timmy)

# Set the shape and color of the turtle
timmy.shape("turtle")
timmy.color("coral")

# Move the turtle forward by 100 units
timmy.forward(100)

# Create a Screen object to display the turtle graphics
my_screen = Screen()

# Print the height of the canvas
print(my_screen.canvheight)

# Wait for a click on the screen to exit
my_screen.exitonclick()
