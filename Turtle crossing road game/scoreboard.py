FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_level()

    def create_level(self):
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.create_level()

    def game_finish(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=FONT)

