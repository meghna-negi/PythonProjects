from turtle import Turtle
import random

#Class to create a ball, move it and detect the collision with wall and paddle
class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    #Function to move ball by increasing x and y coordinate by 10          
    def move_ball(self) -> None:
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    #Function to move ball in opposite direction by changing the y coordinate
    def wall_collision(self) -> None:
        self.y_move *= -1
    
    #Function to move ball in opposite direction by changing the x coordinate
    def paddle_collision(self) -> None:
        self.x_move *= -1

    #Function to place ball at origin and then move in opposite direction,
    #when paddle misses
    def reset_ball(self) -> None:
        self.goto(0,0)
        self.paddle_collision()
