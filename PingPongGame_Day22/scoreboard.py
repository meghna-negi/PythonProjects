from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self,scoreboard_position) -> None:
        super().__init__()
        self.scoreboard_pos = scoreboard_position
        self.score = 0
        self.display_score()
    
    def display_score(self):
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(self.scoreboard_pos)
        self.write(f"SCORE:{self.score}",align=ALIGNMENT,font=FONT)

