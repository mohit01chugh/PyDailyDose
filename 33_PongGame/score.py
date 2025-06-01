from turtle import Turtle

# Constants for alignment and font style
ALINGMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.leftscore = 0  # Initialize left player's score
        self.rightscore = 0  # Initialize right player's score
        self.color("white")  # Set the color of the scoreboard
        self.penup()  # Prevent drawing lines while moving
        self.hideturtle()  # Hide the turtle cursor
        self.display_board()  # Display the initial score board
        
    def display_board(self):
        # Display the current scores on the board
        self.goto(-100, 200)  # Position for left score
        self.write(f"{self.leftscore}", True, align=ALINGMENT, font=FONT)  # Write left score
        self.goto(100, 200)  # Position for right score
        self.write(f"{self.rightscore}", True, align=ALINGMENT, font=FONT)  # Write right score

    def left_point_add(self):
        # Increment left player's score and update the display
        self.leftscore += 1
        self.clear()  # Clear previous scores
        self.display_board()  # Update the display with new scores

    def right_point_add(self):
        # Increment right player's score and update the display
        self.rightscore += 1
        self.clear()  # Clear previous scores
        self.display_board()  # Update the display with new scores

    def game_over(self):
        # Display game over message
        self.goto(0, 0)  # Center position for game over message
        self.write(f"Game Over", True, align=ALINGMENT, font=FONT)  # Write game over message
