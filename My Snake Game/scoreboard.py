from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score: {self.high_score}",align= ALIGNMENT,font= FONT )

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!",align= ALIGNMENT,font= FONT )


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            new_high_score = str(self.high_score)
            with open("data.txt","w") as file:
                file.write(new_high_score)
            self.score = 0
        self.update_scoreboard()
