from turtle import Turtle

#Constants to initialise position of snake body at the beginning of game 
# and distance to move forward
SNAKE_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20

#Class to create, move and extend the snake
class Snake:
    def __init__(self) -> None:
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    #Functions to create the body of snake and extend it when snake collides with food
    def create_snake(self) -> None:
        for position in SNAKE_POS:
            self.add_square(position)
    
    def add_square(self, position) -> None:
        new_square = Turtle(shape = 'square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.snake_body.append(new_square)

    def extend_snake(self) -> None:
        self.add_square(self.snake_body[-1].position())   
    
    #Function to make snake move forward in the current direction
    def move_snake(self) -> None:
        for square in range(len(self.snake_body)-1,0,-1):
            self.snake_body[square].goto(self.snake_body[square-1].xcor(),self.snake_body[square-1].ycor())
        self.head.forward(MOVE_DIST)

    #Functions to move the snake up, down, left and right
    def move_up(self) -> None:
        if(self.head.heading() != 270):
            self.head.setheading(90)

    def move_down(self) -> None:
        if(self.head.heading() != 90):
            self.head.setheading(270)

    def move_left(self) -> None:
        if(self.head.heading() != 0):
            self.head.setheading(180)

    def move_right(self) -> None:
        if(self.head.heading() != 180):
            self.head.setheading(0)
        
     

        


