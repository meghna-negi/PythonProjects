from turtle import Turtle, Screen

turt = Turtle()

#Functions for the movements of sketch
def move_forward()-> None:
    turt.forward(10)

def move_backward()-> None:
    turt.backward(10)

def move_counter_clockwise()-> None:
    turt.left(10)

def move_clockwise()-> None:
    turt.right(10)    

def main()-> None:
    #Creating object for the screen and starting listening
    screen = Screen()
    screen.listen()

    #Defining the event based actions
    screen.onkey(fun = move_forward, key = "w")
    screen.onkey(fun = move_backward, key = "s")
    screen.onkey(fun = move_counter_clockwise, key = "a")
    screen.onkey(fun = move_clockwise, key = "d")
    screen.onkey(fun = screen.resetscreen, key = "c")

    screen.exitonclick()

if __name__ == "__main__":
    main()

