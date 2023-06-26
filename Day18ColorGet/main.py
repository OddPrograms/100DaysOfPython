import colorgram
from turtle import Turtle, Screen, colormode
import random

def dots(turtle, colors):
    for i in range(1, 11):
        turtle.dot(20, random.choice(colors))
        turtle.up()
        turtle.forward(50)
        turtle.down()

def lineup(turtle):
    turtle.left(90)

def main():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        rgb_colors.append(color.rgb)

    paint = Turtle()
    paint.hideturtle()
    paint.speed("fastest")
    colormode(255)
    screen = Screen()


    for i in range(1, 11):
        dots(paint, rgb_colors)
        paint.up()
        paint.setpos(0, i*50)

    screen.exitonclick()

if __name__ == "__main__":
    main()