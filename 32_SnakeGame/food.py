from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set shape of food
        self.penup()  # Disable drawing when moving
        self.shapesize(0.5)  # Make food smaller
        self.color("blue")  # Set food color
        self.speed("fastest")  # Set animation speed
        self.refersh()  # Place food at random position initially

    def refersh(self):
        # Move food to a new random position inside boundaries
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)
