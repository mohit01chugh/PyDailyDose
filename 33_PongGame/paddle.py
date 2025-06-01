from turtle import Turtle

# Initial positions for the paddles
Initalze_postions = [(350, 0), (-350, 0)]
Move_dist = 20  # Movement distance for the paddles
UP = 90  # Direction constant for up
DOWN = 270  # Direction constant for down

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")  # Set shape of the paddle
        self.color("white")  # Set paddle color
        self.shapesize(stretch_wid=5, stretch_len=1)  # Set size of the paddle
        self.penup()  # Disable drawing when moving
        self.goto(position)  # Move paddle to the specified position
            
    def direction_up(self):
        # Move the paddle up by 20 units
        new_y = self.ycor() + 20  # Calculate new y position
        self.goto(self.xcor(), new_y)  # Move paddle to new position

    def direction_down(self):
        # Move the paddle down by 20 units
        new_y = self.ycor() - 20  # Calculate new y position
        self.goto(self.xcor(), new_y)  # Move paddle to new position
