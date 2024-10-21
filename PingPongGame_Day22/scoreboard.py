from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 30, 'normal')

#Class for creating and updating scoreboard of the two players
#Inherits from the turtle class
class Scoreboard(Turtle):
    def __init__(self,scoreboard_position) -> None:
        super().__init__()
        self.scoreboard_pos = scoreboard_position
        self.score = 0
        self.display_score()
    
    def display_score(self) -> None:
        self.clear()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(self.scoreboard_pos)
        self.write(f"{self.score}",align=ALIGNMENT,font=FONT)
        
    def final_score(self, player) -> None:
        self.goto(0,0)
        self.write(f"{player} won",align=ALIGNMENT,font=FONT)

