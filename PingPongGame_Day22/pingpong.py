from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Positions of Paddle
POSITIONS = [(380,0),(-380,0)]

def main() -> None:
    #Creating objects for the Screen and adjusting its properties
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.title("Classic PingPong game")
    screen.bgcolor('black')
    screen.listen()
    screen.tracer(0)

    #Creating Turtle object for drawing the partition line on screen
    turt = Turtle(shape = 'square')
    turt.speed(0)
    turt.hideturtle()
    turt.color('white')
    turt.penup()
    turt.goto(0,280)
    turt.right(90)
    for _ in range(18):
        turt.pendown()
        turt.forward(20)
        turt.penup()
        turt.forward(20)

    #Creating Paddle objects for two players
    player1 = Paddle(POSITIONS[0])
    player2 = Paddle(POSITIONS[1])

    #Flag to continue the game and key presses to move the paddles
    game_on = True
    screen.onkey(fun=player1.move_up, key= 'Up')
    screen.onkey(fun=player1.move_down, key= 'Down')
    screen.onkey(fun=player2.move_up, key= 'w')
    screen.onkey(fun=player2.move_down, key= 's')

    #Creating Scoreboard object and displaying the score
    score1 = Scoreboard((150,260))
    score2 = Scoreboard((-150,260))
    score1.display_score()
    score2.display_score()

    #Creating Ball object 
    ball = Ball()
  
    while(game_on):
        screen.update()
        time.sleep(0.05)

        #Moving ball until the game_on is not set to False
        ball.move_ball()

        #Detecting the collision of ball with ball and bouncing the ball
        if(ball.ycor()>280 or ball.ycor()<-280):
            ball.wall_collision()

        #Detecting the collision of ball with the paddle of either player
        if(ball.distance(player1.player.position())<50 and ball.xcor()>340 or ball.distance(player2.player.position())<50 and ball.xcor()<-340):
            ball.paddle_collision()

        #If either player misses the ball, reset the ball and move it in opposite direction
        #Increase the score of the opposite player
        if(ball.xcor()>380):
            ball.reset_ball()
            score2.score += 1
            score2.display_score()    

        if(ball.xcor()<-380):
            ball.reset_ball()
            score1.score += 1
            score1.display_score()

        #Whichever player score 10 points first wins the match and game finishes
        if(score1.score == 10):
            score1.final_score('Right Player')
            game_on = False

        if(score2.score == 10):
            score2.final_score('Left Player')
            game_on = False


    screen.exitonclick()

if __name__ == "__main__":
    main()
