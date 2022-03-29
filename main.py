from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
score_board = ScoreBoard()
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title(" Tesfay Pong Game")

screen.setup(width=800, height=600, startx=0, starty=0)

r_paddle = Paddle((350, 0), "Up", "Down")
l_paddle = Paddle((-350, 0), "w", "s")
ball = Ball()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if the r_paddle misses the ball
    if ball.xcor() > 350:
        ball.re_fresh()
        score_board.l_point()
    # detect if the l_paddle misses the ball
    if ball.xcor() < -350:
        ball.re_fresh()
        score_board.r_point()













screen.exitonclick()