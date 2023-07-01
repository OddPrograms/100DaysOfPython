from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
from food import Food
import time

def clear():
    snake.up()
    snake.clear()
    snake.home()
    snake.down()

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake The Game")
    screen.tracer(0)
    starting_position = [(0, 0), (-20, 0), (-40, 0)]

    global snake
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    playing = True
    while playing:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            playing = False
            scoreboard.game_over()

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                playing = False
                scoreboard.game_over()

    screen.exitonclick()

if __name__ == "__main__":
    main()