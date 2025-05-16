from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the game screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)  # Disable automatic screen updates for manual control

# Initialize game components
snake = Snake()
food = Food()
score = Scoreboard()

# List to hold snake segments
segments = []

# Set up keyboard controls
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_on = True
while game_on:
    screen.update()  # Refresh the screen
    time.sleep(0.5)  # Control the game speed

    snake.move()  # Move the snake
    
    # Check for collision with food
    if snake.head.distance(food) < 15:
        food.refersh()  # Refresh food position
        snake.extend_segment()  # Add segment to the snake
        score.score_add()  # Update score

    # Check for collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
       snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.resetHigh()  # Reset score
        snake.resetsk()  # Reset snake position

    # Check for collision with itself
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass  # Ignore the head
        elif snake.head.distance(segment) < 10:
            score.resetHigh()  # Reset score
            snake.resetsk()  # Reset snake position

# Exit the game on click
screen.exitonclick()
