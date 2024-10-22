import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Creating Screen object
screen = Screen()

def main() -> None:

    #Setting the flag to continue the movement of snake
    game_on = True

    #Setting the properties of the screen
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("Classic snake Game")
    screen.tracer(0)
    screen.listen()
    
    #Creating objects for Snake, Food and Scoreboard classes
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    #Creating events for pressing of up, down, left and right arrow keys
    screen.onkey(fun = snake.move_up, key = 'Up')
    screen.onkey(fun = snake.move_down, key = 'Down')
    screen.onkey(fun = snake.move_left, key = 'Left')
    screen.onkey(fun = snake.move_right, key = 'Right')

    #Continue the movement of snakes till the flag is set True
    while game_on:
        #Setting the screen property and sleepin time for stable animation
        screen.update()
        time.sleep(0.1)

        #Moving the snake forward
        snake.move_snake()
        
        #Creating new food, extending snake body and updating the score when colliding with current food
        if(snake.head.distance(food)<=15):
            food.new_food()
            snake.extend_snake()
            scoreboard.score += 1
            scoreboard.display_score()
        
        #Resetting game and snake in case snake collides with screen boundaries
        if(snake.head.xcor()>= 280 or snake.head.xcor()<=-280 or snake.head.ycor()>= 280 or snake.head.ycor()<=-280):
            scoreboard.reset_game()
            snake.reset_snake()

        #Resetting game and snake in case snake collides with its own body
        for square in snake.snake_body[1:]:
            if(snake.head.distance(square) < 10):
                scoreboard.reset_game()
                snake.reset_snake()


    screen.exitonclick()
    

if __name__ == "__main__":
    main()