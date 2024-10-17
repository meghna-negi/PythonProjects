from turtle import Turtle,Screen
import random

#Function to conduct a turtle race
def get_winner(all_turtles, race) -> tuple:
    #Shuffling list so that first element of list(red) doesn't always get updated first 
    random.shuffle(all_turtles)

    #Starting and continuing the race until a turtle crosses the finish line
    while(race == True):
        for turt in all_turtles:
            if(turt.xcor()>230):
                return(turt.color())
            else:
                turt.forward(random.randint(0,10))

def main() -> None:
    #Creating screen object and adjusting properties
    screen = Screen()
    screen.setup(width=500, height=400)

    #Getting users input
    user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a colour:")

    colours = ["red", "blue", "yellow", "green", "purple", "orange"]
    y_cor = [120, 80, 40, 0, -40, -80]
    race = True
    all_turtles = []

    #Creating turtle objects and adjusting the properties
    for index in range(len(colours)):
        turt = Turtle(shape = 'turtle')
        turt.color(colours[index])
        turt.penup()
        turt.goto(-240, y_cor[index])
        all_turtles.append(turt)

    #Starting the race and getting the winner
    winner = get_winner(all_turtles,race)

    #Check if the users bet is the winner or not
    if(user_bet == winner[0]):
        print("You won the bet!!!!")
    else:
        print(f"{winner[0]} wins. You lost the bet.")

    screen.exitonclick()

if __name__ == "__main__":
    main()