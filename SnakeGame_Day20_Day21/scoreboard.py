from turtle import Turtle

#Constants used in this class
ALIGNMENT = 'center'
FONT = ('Arial', 18, 'normal')
SCOREBOARD_POSITION = (0,260)
GAMEOVER_POSITION = (0,0)

#Class to create and display the current score, inherits Turtle class
class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = -1
        self.display_score()
    
    #Function to increase and display the score at the upper center of the screen
    def display_score(self) -> None:
        self.clear()
        self.score = self.score + 1
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.write(f"Score:{self.score}",align=ALIGNMENT,font=FONT)

    #Function to display game over when collision with boundary or snake's body happens
    def display_game_over(self) -> None:
        self.goto(GAMEOVER_POSITION)
        self.write("Game over",align=ALIGNMENT,font=FONT)
