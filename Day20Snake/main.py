from turtle import Screen
from snake import Snake
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

    screen.exitonclick()

if __name__ == "__main__":
    main()