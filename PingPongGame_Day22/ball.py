from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.speed(2)
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(0,-280)
        
    def move_ball(self):
        self.goto(280,random.randint(-280,280))
        self.goto(0,-280)
        self.goto(-280,random.randint(-280,280))
        self.goto(0,-280)