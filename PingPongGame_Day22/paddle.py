from turtle import Turtle

#Class to create paddle for players and moving them
class Paddle:
    def __init__(self, player_position) -> None:
        self.player = Turtle(shape = 'square')
        self.player_position = player_position
        self.create_paddle()

    def create_paddle(self) -> None:
        self.player.speed(6)
        self.player.setheading(90)
        self.player.resizemode("user")
        self.player.shapesize(1,5,1)
        self.player.color('white')
        self.player.penup()
        self.player.goto(self.player_position)

    def move_up(self) -> None:
        if(self.player.ycor()<280):
            self.player.forward(20)

    def move_down(self) -> None:
        if(self.player.ycor()>-280):
            self.player.backward(20)