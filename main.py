from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-375, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 400 or ball.ycor() < -400:
        ball.bounce_on_shelves()
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 350) or (ball.distance(l_paddle) < 60 and ball.xcor() < -350):
        ball.bounce_on_paddle()
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_is_on = False
        screen.clear()
announcement = Turtle()
if scoreboard.l_score == 10:
    announcement.write("Player 1 wins!!")
else:
    announcement.write("Player 2 wins!!")

