from turtle import Turtle, Screen, position
from random import randint

tim = Turtle()
scrren = Screen()
scrren.colormode(255)  # Set color mode to RGB

# Generate a random RGB color
def colors():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

# Draw multiple circles with colors in a circular pattern
def draw_graph(Num_of_gaps):
    for _ in range(int(360 / Num_of_gaps)):
        tim.color(colors())  # Set random color
        tim.circle(100)  # Draw a circle of radius 100
        tim.speed("fastest")  # Set speed to fastest
        tim.setheading(tim.heading() + 10)  # Rotate turtle by 10 degrees

draw_graph(10)  # Draw pattern with 10-degree gaps
scrren.exitonclick()  # Wait for click to exit
