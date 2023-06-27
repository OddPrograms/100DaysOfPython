import turtle
from turtle import Turtle, Screen

def move_forwards():
    painter.forward(10)

def move_backwards():
    painter.backward(10)

def turn_left():
    new_heading = painter.heading() + 10
    painter.setheading(new_heading)

def turn_right():
    new_heading = painter.heading() - 10
    painter.setheading(new_heading)

def clear():
    painter.up()
    painter.clear()
    painter.home()
    painter.down()

def main():
    global painter
    painter = Turtle()
    screen = Screen()


    screen.listen()
    screen.onkey(fun=move_forwards, key="w")
    screen.onkey(fun=move_backwards, key="s")
    screen.onkey(fun=turn_left, key="a")
    screen.onkey(fun=turn_right, key="d")
    screen.onkey(fun=clear, key="c")
    screen.exitonclick()


if __name__ == "__main__":
    main()