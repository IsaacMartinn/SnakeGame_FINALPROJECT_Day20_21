from turtle import Turtle

ALLIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.teleport(x=0, y=260)

    def current_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALLIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(x=0, y=0)
        self.write("GAME OVER", move=False, align=ALLIGNMENT, font=FONT)
