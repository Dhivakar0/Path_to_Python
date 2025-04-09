from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def increase_l_score(self):
        self.l_score += 1
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(arg=self.l_score,align="center", font=("Arial", 36, "normal"))
        self.goto(100,250)
        self.write(arg=self.r_score,align="center", font=("Arial", 36, "normal"))




