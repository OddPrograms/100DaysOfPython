from turtle import Turtle

class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("honeydew4")
        self.penup()
        self.shapesize(-25, 50)