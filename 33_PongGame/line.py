from turtle import Turtle

class Lineup(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")  # Set color of the lineup
        self.penup()  # Disable drawing when moving
        self.hideturtle()  # Hide the turtle cursor
        self.pensize(2)  # Set the pen size for drawing
        self.goto(0, -300)  # Move to the starting position
        self.setheading(90)  # Set direction to upward
        self.draw()  # Call the draw method to create the lineup

    def draw(self):
        # Draw a dashed line by alternating pen down and pen up
        for _ in range(32):
            self.pendown()  # Start drawing
            self.forward(10)  # Move forward while drawing
            self.penup()  # Stop drawing
            self.forward(10)  # Move forward without drawing
