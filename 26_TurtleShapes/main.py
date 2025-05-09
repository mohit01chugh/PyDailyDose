from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()
screen.colormode(255)  # Use RGB color mode (0-255)

def colors():
    # Generate random RGB color tuple
    return (randint(0, 255), randint(0, 255), randint(0, 255))

i = 0
def draw_shape():
    # Draw a polygon with (3 + i) sides
    for _ in range(3 + i):
        tim.forward(100)
        angle = 360 / (3 + i)  # Calculate angle for polygon
        tim.right(angle)

# Draw polygons with sides from 3 to 7, changing color each time
for s in range(5):
    draw_shape()
    i += 1
    tim.color(colors())

# Wait for a click to exit
screen.exitonclick()
