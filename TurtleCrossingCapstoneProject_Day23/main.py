import time
from turtle import Turtle,Screen
from player import Player
from cars import Cars

cars = []
ALIGNMENT = "center"
FONT = ("Courier",20,"normal")

def main() -> None:
    #Initializing speed and level of the game
    speed = 10
    level = 0

    #Creating Screen object and adjusting the properties
    screen = Screen()
    screen.title("Turtle Crossing Capstone Game")
    screen.setup(width=600,height=600)
    screen.colormode(255)
    screen.listen()
    screen.tracer(0)

    #Creating Turtle object for displaying Level on screen
    Level = Turtle()
    Level.penup()
    Level.hideturtle()

    #Setting the flag to continue the game and creating Player object    
    game_on = True
    player = Player()

    #Creating instances of Cars class
    for _ in range(20):
        new_car = Cars()
        cars.append(new_car)

    screen.onkey(fun=player.move_player, key='Up')

    while(game_on):
        screen.update()
        time.sleep(0.1)

        #Show the current level
        Level.clear()
        Level.goto(-220,240)
        Level.write(f"Level {level}",align=ALIGNMENT,font=FONT)
        
        #Moving all the instances of car at a speed decided by level 
        for car in cars:
            car.move_car(speed)

            #To detect collision of turtle with car and stop the game
            if(player.distance(car) < 23):
                game_on = False
                player.penup()
                player.goto(0,0)
                player.write("Game Over",align=ALIGNMENT,font=FONT)

            #To check if players crosses the level and starts next difficulty level
            if(player.ycor()>290):
                speed += 5
                player.goto(0,-280)
                level += 1

    screen.exitonclick()

if __name__ == "__main__":
    main()
