from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)

screen.listen()
paddle_r = Paddle((375, 0))
paddle_l = Paddle((-383, 0))
ball = Ball()
score = Scoreboard()

screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_the_ball()

    # Detect the collision with the y_wall.
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    # Detect the collision with the paddles
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 350) or (ball.distance(paddle_l) < 50 and ball.xcor() < -360):
        ball.bounce_x()
        if ball.distance(paddle_r) < 50 and ball.xcor() > 350:
            paddle_r.color(ball.col)
        elif ball.distance(paddle_l) < 50 and ball.xcor() < -360:
            paddle_l.color(ball.col)

    # Detect the collision with the x_walls.
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        paddle_r.color("white")
        paddle_l.color("white")
    elif ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        paddle_r.color("white")
        paddle_l.color("white")
    if score.l_score == 10 or score.r_score == 10:
        game_is_on = False
        score.game_over()

screen.exitonclick()
