from turtle import Turtle, Screen

#Function to draw dashed line
def Draw_Dashed_Line(turtle_obj, line_length, part_length, gap_length)-> None:

    # Put the pendown to draw line & penup for dash part
    for _ in range(line_length):
        turtle_obj.pendown()
        turtle_obj.forward(part_length)
        turtle_obj.penup()
        turtle_obj.forward(gap_length)


def main():

    #Creating Turtle object and changing properties
    turt = Turtle()
    turt.shape("arrow")

    #Length of dashed line, length of contiuous line, length of gap
    length = 50
    part_length = 5
    gap_length = 5

    Draw_Dashed_Line(turt, length, part_length, gap_length)

    my_screen = Screen()
    my_screen.exitonclick()

if __name__ == "__main__":
    main()