from turtle import Turtle

FONT = ("Times New Roman", 16, "bold")
SCOREBOARD_POSITION = (-245, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setposition(SCOREBOARD_POSITION)
        self.level = 1
        self.update_scoreboard()

    def update_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
