from turtle import Screen
from line import Lineup
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Initialize game components
line = Lineup()  # Create the center line
left_paddle = Paddle((-350, 0))  # Create left paddle
right_paddle = Paddle((350, 0))  # Create right paddle
ball = Ball()  # Create the ball
score = Scoreboard()  # Create the scoreboard

# Set up the screen
screen = Screen()
screen.listen()  # Listen for key presses
screen.tracer(0)  # Disable automatic screen updates
screen.bgcolor("black")  # Set background color
screen.setup(800, 600)  # Set screen size
screen.title("The Famous Pong Game")  # Set window title

# Set up key bindings for paddle movement
screen.onkey(key="a", fun=left_paddle.direction_up)  # Move left paddle up
screen.onkey(key="z", fun=left_paddle.direction_down)  # Move left paddle down
screen.onkey(key="p", fun=right_paddle.direction_up)  # Move right paddle up
screen.onkey(key="l", fun=right_paddle.direction_down)  # Move right paddle down

# Main game loop
game_on = True
while game_on:
    screen.update()  # Update the screen
    time.sleep(ball.move_speed)  # Control the speed of the ball
    ball.move()  # Move the ball
            
    # Bounce the ball off the top and bottom walls
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bouce_y()  # Reverse ball's vertical direction
    
    # Check for collisions with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bouce_x()  # Reverse ball's horizontal direction
        score.right_point_add()  # Update right player's score        
    elif ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bouce_x()  # Reverse ball's horizontal direction
        score.left_point_add()  # Update left player's score

    # Reset ball if it goes out of bounds
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.resetting()  # Reset ball position
            
screen.exitonclick()  # Exit on click
