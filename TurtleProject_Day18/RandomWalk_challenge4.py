from turtle import Turtle,Screen
import random

#Function to generate random colour based on rgb values
def random_color() -> tuple:
    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

#Function to generate random walk
def random_walk(turtle_obj) -> None:
    #A list with four different directions
    directions = [0,90,180,270]

    #Assigning random colour to the lines which move 30 steps in any random direction
    for _ in range(50):
        turtle_obj.color(random_color())
        turtle_obj.forward(30)
        turtle_obj.setheading(random.choice(directions))

def main():
    #Creating object for Turtle class and adjusting properties
    turt = Turtle()
    turt.shape('classic')
    turt.pensize(20)
    turt.speed(0)

    #Creating object for Screen class and adjusting property
    my_screen = Screen()
    my_screen.colormode(255)

    random_walk(turt)

    my_screen.exitonclick()

if __name__ == "__main__":
    main()