from turtle import Turtle

ALINGMENT = "center"  # Text alignment for game over message
spd = 10  # Speed variable (not used in this code)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set shape of the ball
        self.color("blue")  # Set ball color
        self.shapesize(stretch_wid=1, stretch_len=1)  # Set size of the ball
        self.penup()  # Disable drawing when moving
        self.goto(0, 0)  # Start position of the ball
        self.x_move = 10  # Horizontal movement speed
        self.y_move = 10  # Vertical movement speed
        self.move_speed = 0.1  # Initial move speed

    def move(self):
        # Move the ball based on its current speed
        new_x = self.xcor() + self.x_move  # Calculate new x position
        new_y = self.ycor() - self.y_move  # Calculate new y position
        self.goto(new_x, new_y)  # Move the ball to the new position

    def bouce_y(self):
        # Reverse the vertical direction of the ball
        self.y_move *= -1

    def bouce_x(self):
        # Reverse the horizontal direction of the ball and increase speed
        self.x_move *= -1
        self.move_speed *= 0.9  # Increase speed slightly

    def resetting(self):
        # Reset the ball to the center and reverse its horizontal direction
        self.goto(0, 0)  # Move to the center
        self.move_speed = 0.1  # Reset move speed
        self.bouce_x()  # Reverse horizontal direction

    def game_over(self):
        # Display game over message at the center
        self.goto(0, 0)  # Center the message
        self.write(f"Game Over", True, align=ALINGMENT)  # Write game over message
