from turtle import Turtle,Screen

#Simple code to draw a square of a given length
def draw_square(turtle_obj, length)-> None:
    for _ in range(4):
        turtle_obj.forward(length)
        turtle_obj.left(90)

def main():
    square_side = float(input("Enter the length of the side of the square \n"))

    #Creating the objects for Turtle and Screen, calling method to draw square
    turt = Turtle()
    turt.shape("turtle")

    draw_square(turt, square_side)

    my_screen = Screen()
    my_screen.exitonclick()

if __name__ == "__main__":
    main()