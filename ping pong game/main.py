import time
from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # print(ball.position())

# Detect collisions with top and bottom walls.

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

# Detect collisions with paddles.
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        ball.bounce_x()

 # Detect when right paddle misses the ball.
    if ball.xcor() > 380:
        ball.restart()
        score.increase_l_score()

# #  Detect when left paddle misses the ball.
    if ball.xcor() < -380:
        ball.restart()
        score.increase_r_score()


screen.exitonclick()