from turtle import Turtle

#Class to create a player and move the player by 10 in north direction
class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def move_player(self) -> None:
        self.forward(10)