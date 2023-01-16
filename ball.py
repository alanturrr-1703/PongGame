import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.x_move = 0.03
        self.y_move = 0.06

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_on_shelves(self):
        self.y_move *= -1

    def bounce_on_paddle(self):
        self.x_move *= random.randint(3, 6) * -0.3

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_on_paddle()

