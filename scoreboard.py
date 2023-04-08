from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 230)
        self.write(f"{self.l_score}", align="center", font=("courier", 40, "normal"))
        self.goto(50, 230)
        self.write(f"{self.r_score}", align="center", font=("courier", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=("courier", 20, "normal"))
