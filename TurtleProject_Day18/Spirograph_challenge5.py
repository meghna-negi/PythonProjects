from turtle import Turtle, Screen
import random

#Function to generate random colour based on rgb values
def random_color() -> tuple:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return(r,g,b)

#Function to draw a spirograph based on the gap size between each circle
def draw_spirograph(turtle_obj, gap_size)-> None:

    #Drawing circle and moving the pointer to left based on gap_size degrees 
    for _ in range(int(360/gap_size)):
        turtle_obj.color(random_color())
        turtle_obj.circle(100)
        turtle_obj.left(gap_size)


def main():

    #Creating the object for Turtle and setting the speed of cursor
    turt = Turtle()
    turt.speed(0)

    #Creating the object for Screen and adjusting colormode
    my_screen = Screen()
    my_screen.colormode(255)
    
    draw_spirograph(turt,5)

    my_screen.exitonclick()

if __name__ == "__main__":
    main()