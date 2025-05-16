from turtle import Turtle

ALINGMENT = "center"  # Text alignment for scoreboard

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize current score
        self.highscore = self.readHscore()  # Read high score from file
        self.color("white")  # Set text color
        self.penup()  # Disable drawing when moving
        self.hideturtle()  # Hide the turtle cursor
        self.display_board()  # Display initial score board

    def readHscore(self):
        # Read high score from a file
        with open('highscore.txt', mode='r') as file:
            hscore = file.read()
        return hscore

    def updateHscore(self):
        # Update high score in the file
        with open('highscore.txt', mode='w') as file:
            newhscore = file.write(str(self.score))
        return newhscore

    def resetHigh(self):
        # Reset score and update high score if necessary
        if self.score > int(self.highscore):
            self.highscore = self.score  # Update high score
            self.updateHscore()  # Save new high score
        self.score = 0  # Reset current score
        self.display_board()  # Refresh display

    def display_board(self):
        # Clear previous score and display current score and high score
        self.clear()
        self.goto(0, 280)  # Position the text
        self.write(f"Score = {self.score} || High Score = {self.highscore}", True, align=ALINGMENT)

    def score_add(self):
        # Increment score and update display
        self.score += 1
        self.display_board()

    def game_over(self):
        # Display game over message
        self.goto(0, 0)  # Center the message
        self.write(f"Game Over", True, align=ALINGMENT)
