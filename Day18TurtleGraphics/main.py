import random
import turtle
from turtle import Turtle, Screen
from random import Random

def overlayed_shapes(num_sides, turtle):
    angle = 360 / num_sides
    for i in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

def shapes_algorithm(turtle, colors):
    for shape_side_n in range(3, 11):
        turtle.color(random.choice(colors))
        overlayed_shapes(shape_side_n, turtle)

def random_walk(turtle):
    directions = [0, 90, 180, 270]
    turtle.width(15)
    for i in range(500):
        turtle.forward(30)
        turtle.setheading(random.choice(directions))
        turtle.color(random_color())
        # turtle.color(random.choice(colors))

def spirograph(turtle, size_of_gap):
    for i in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color

def main():
    screen = Screen()
    turtle.screensize(1920, 1080)
    # screen.bgcolor("LightSlateGrey")
    # colors = [
    #     "#1C1C1C",
    #     "#DADDD8",
    #     "#ECEBE4",
    #     "#EEF0F2",
    #     "#FAFAFF",
    # ]
    my_turtle = Turtle()
    turtle.colormode(255)
    my_turtle.speed("fastest")

    spirograph(my_turtle, random.randint(1, 10))

    # random_walk(my_turtle)

    # shapes_algorithm(my_turtle, colors)

    screen.exitonclick()

if __name__ == "__main__":
    main()