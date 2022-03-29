
from turtle import Turtle, Screen
screen = Screen()

class Paddle(Turtle):

    def __init__(self, position, up_key, down_key):
        super().__init__()
        self.up_key = up_key
        self.down_key = down_key
        self.shape("square")
        self. paddle_width = 5
        self. paddle_height = 1
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=self.paddle_width, stretch_len=self.paddle_height)
        self.goto(position)
        self.paddle_move()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def paddle_move(self):
        screen.listen()
        screen.onkey(self.up, self.up_key)
        screen.onkey(self.down, self.down_key)
