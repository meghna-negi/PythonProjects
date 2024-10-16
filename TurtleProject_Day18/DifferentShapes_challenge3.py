from turtle import Turtle, Screen
import random 

#Function to generate random colour based on rgb values
def random_color() -> tuple:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

#Function to generate different polygons, taking sides as argumeny
def drawPolygon(turtle_obj,sides) -> None:
    #Draw different lines for polygons based on number of sides
    #Tilting cursor in a angle based on number of sides
    for _ in range(sides):
        turtle_obj.forward(100)
        angle = 180 - (((sides-2)* 180)/sides)
        turtle_obj.right(angle)

def main():
    #Creating objects for Turtle and Screen and adjust properties
    turt = Turtle()
    turt.shape("arrow")
    my_screen = Screen()
    my_screen.colormode(255)    

    #Calling the drawPolygon with different colours and differeny number of sides
    for side in range(3,11):
        turt.color(random_color())
        drawPolygon(turt, side)

    my_screen.exitonclick()

if __name__ == "__main__":
    main()
