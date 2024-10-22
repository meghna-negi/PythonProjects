from turtle import Turtle
import random

#Class for creating the cars and move them, inherits Turtle
class Cars(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.shape('square')
        self.setheading(180)
        self.resizemode("user")
        self.shapesize(1,2,1)
        self.penup()
        self.speed(5)
        self.goto(random.randrange(320,900,40), random.randrange(-250,250,50))
    
    #Function to move forward, reset the cars when exit from left
    #Steps to move forward act as speed of the cars
    def move_car(self,speed) -> None:
        if(self.xcor()>-300):
            self.forward(speed)
        else:
            self.goto(random.randrange(320,900,40), random.randrange(-250,250,50))
