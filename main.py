from turtle import Screen
from Paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game, Felipe Cortés")
screen.tracer(0)  # To turn off animations

player_1 = Paddle(1)
player_2 = Paddle(2)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")
screen.onkey(player_2.go_up, "w")
screen.onkey(player_2.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(player_1) < 50 and ball.xcor() > 325 or ball.distance(player_2) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 350:
        score.l_point()
        time.sleep(0.4)
        ball.reset_ball()

    # Detect when left paddle misses
    if ball.xcor() < -350:
        score.r_point()
        time.sleep(0.4)
        ball.reset_ball()

screen.exitonclick()