from turtle import Turtle
import random

#Class to create food at random points on the screen, inherits Turtle class
class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(0)
        self.new_food()
        

    def new_food(self) -> None:
        self.goto(random.randint(-280,280),random.randint(-280,280))


