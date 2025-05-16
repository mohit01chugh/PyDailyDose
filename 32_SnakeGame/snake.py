from turtle import Turtle

# Initial positions of the snake segments
Initalze_postions = [(0, 0), (-20, 0), (-40, 0)]
Move_dist = 20  # Distance the snake moves
UP = 90  # Direction constants
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []  # List to hold snake segments
        self.spd = 1  # Speed of the snake (not used in this code)
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # Set the head of the snake

    def create_snake(self):
        # Create the snake segments at initial positions
        for position in Initalze_postions:
            self.add_segement(position)

    def add_segement(self, position):
        # Add a new segment to the snake at the given position
        snake = Turtle("square")  # Create a square turtle
        snake.color("white")  # Set segment color
        snake.penup()  # Disable drawing when moving
        snake.goto(position)  # Move segment to the specified position
        self.segments.append(snake)  # Add segment to the list

    def extend_segment(self):
        # Add a new segment at the position of the last segment
        self.add_segement(self.segments[-1].position())

    def move(self):
        # Move the snake by updating the position of each segment
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get x-coordinate of the segment in front
            new_y = self.segments[seg_num - 1].ycor()  # Get y-coordinate of the segment in front
            self.segments[seg_num].goto(new_x, new_y)  # Move current segment to the new position
        self.head.forward(Move_dist)  # Move the head forward

    def resetsk(self):
        # Reset the snake to its initial state
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move segments off-screen
        self.segments.clear()  # Clear the segment list
        self.create_snake()  # Recreate the snake
        self.head = self.segments[0]  # Reset the head

    def up(self):
        # Change direction to up if not already moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change direction to down if not already moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change direction to left if not already moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change direction to right if not already moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
