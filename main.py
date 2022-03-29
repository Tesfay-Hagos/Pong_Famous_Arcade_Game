from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title(" Tesfay Pong Game")

screen.setup(width=800, height=600, startx=0, starty=0)

paddle = Paddle((350, 0) , "Up", "Down")
paddle2 = Paddle((-350, 0), "w", "s")
ball = Ball()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.refresh_ball()
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce()










screen.exitonclick()