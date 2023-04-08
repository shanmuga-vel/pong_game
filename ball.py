from turtle import Turtle
import random
COLORS = ["red", "blue", "sky blue", "gray", "yellow", "orange"]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.col = ""
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_the_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.col = random.choice(COLORS)
        self.color(self.col)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.color("white")
