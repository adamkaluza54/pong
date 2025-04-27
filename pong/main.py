from turtle import Screen, Turtle
from rackets import Rackets
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

racket_right = Rackets(350)
racket_left = Rackets(-350)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(racket_right.move_up, "Up")
screen.onkeypress(racket_right.move_down, "Down")

screen.onkeypress(racket_left.move_up, "w")
screen.onkeypress(racket_left.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move_ball()

#Detect collision with up and down wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#Detect collision wt=ith the racket
    if ball.distance(racket_right) < 50 and ball.xcor() > 320 or ball.distance(racket_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor()> 400:
        score.increase_left_score()
        ball.reset_position()

    if ball.xcor()< -400:
        score.increase_right_score()
        ball.reset_position()

screen.exitonclick()