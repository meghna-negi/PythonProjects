from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

POSITIONS = [(-280,0),(280,0)]

def main() -> None:
    screen = Screen()
    screen.setup(width = 600, height = 600)
    screen.title("Classic PingPong game")
    screen.bgcolor('black')
    screen.listen()

    player1 = Paddle(POSITIONS[0])
    player2 = Paddle(POSITIONS[1])
    game_on = True

    screen.onkey(fun=player1.move_up, key= 'w')
    screen.onkey(fun=player1.move_down, key= 's')
    screen.onkey(fun=player2.move_up, key= 'p')
    screen.onkey(fun=player2.move_down, key= 'l')

    score1 = Scoreboard((150,280))
    score2 = Scoreboard((-150,280))
    score1.display_score()
    score2.display_score()

    ball = Ball()
  
    while(game_on):

        ball.move_ball()

        player1.ball_collision(ball)

    screen.exitonclick()

if __name__ == "__main__":
    main()
