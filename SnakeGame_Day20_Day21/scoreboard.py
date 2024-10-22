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
        self.score = 0
        with open("highscore.txt",mode='r') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.display_score()
    
    #Function to increase and display the score at the upper center of the screen
    def display_score(self) -> None:
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}",align=ALIGNMENT,font=FONT)

    #Function to update high score, if required
    # and to reset the game     
    def reset_game(self) -> None:
        if(self.score > self.high_score):
            self.high_score = self.score
            with open("highscore.txt",mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()