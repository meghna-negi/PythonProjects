from turtle import Turtle,Screen
import colorgram
import random

#Extracting the colour list from the image to be future used, used only once
def get_rgb_values() -> None:
    col_list = []
    num_col_extracted = 15
    colors = colorgram.extract('hirst_spot_painting_color_pallete.jpg',num_col_extracted)

    for col in range(num_col_extracted):
        rgb_tup = (colors[col].rgb.r,colors[col].rgb.g,colors[col].rgb.b)
        col_list.append(rgb_tup)

def draw_painting(turtle_obj, colour_list) -> None:

    #Hiding the turtle pointer for better visualization and putting penup to not draw line
    turtle_obj.hideturtle()
    turtle_obj.penup()

    #Moving pointer below to adjust full painting
    turtle_obj.goto(-180,-200)

    #Looping to get 10 rows and 10 columns of painting
    for row in range(10):
        for column in range(10):
            turtle_obj.dot(20, random.choice(colour_list))
            turtle_obj.forward(50)

        #Moving the pointer to the starting point's x coordinate, then moving ahead on y axis    
        turtle_obj.setx(-180.0)
        turtle_obj.left(90)
        turtle_obj.forward(50)
        turtle_obj.right(90)

def main():
    #Colour list created using get_rgb_values method
    colour_list = [ (220, 149, 107), (140, 119, 8), (73, 127, 125), (14, 122, 175), (56, 10, 10), (78, 40, 65), (185, 90, 156), (56, 165, 55), (226, 152, 223), (119, 8, 14), (4, 86, 120), (251, 251, 0)]  
    
    #Creating Turtle and Screen objects
    #Changing colourmode to 255 for changing colour using rgb 
    turt = Turtle()
    my_screen = Screen()
    my_screen.colormode(255)

    draw_painting(turt, colour_list)

    my_screen.exitonclick()

if __name__ == "__main__":
    main()