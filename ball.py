
from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)
        self.position= [(0, 350), (350, 350)]

    def refresh_ball(self):
        self.
        self.penup()
        position = random.choice(self.position)
        self.goto(position)
        self.clear()
