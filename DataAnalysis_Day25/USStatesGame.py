from turtle import Turtle, Screen
import pandas as pd

def main() -> None:
    #Counter for correctly guesses states
    state_count = 0

    #Creating turtle object and adjusting its properties
    pointer = Turtle()
    pointer.hideturtle()
    pointer.penup()

    #Creating screen object and adjusting its properties
    screen = Screen()
    screen.setup(width=725,height=491)
    screen.title('US States game')
    screen.bgpic('blank_states_img.gif')

    #Reading the csv file and creating list of all the states
    states = pd.read_csv("50_states.csv")
    state_list = states['state'].to_list()

    #Lists to keep track of correctly guessed and missed states
    guessed_list = []
    missing_list = []

    #Game will run until all states are guessed or user types exit as an input
    while(state_count < 50):

        user_input = screen.textinput(f"{state_count}/50 States Correct","Enter the name of the state")
        #Checking if user gave exit as input
        if(user_input.title() == 'Exit'):
            #Creating the list for all the missed states
            for state in state_list:
                if(state not in guessed_list):
                    missing_list.append(state)

            #Writing the list to the csv and exiting the game
            csv_data = pd.DataFrame(missing_list,columns=['missing states'])
            csv_data.to_csv('MissedStates.csv')
            break
        
        #Finding the users input in the dataframe
        current_state = states[states['state'].str.lower() == user_input.lower()]
        #Proceed only when valid state is entered and has not already been guessed
        if(len(current_state) and user_input not in guessed_list):

            #Getting x and y coordinate of state     
            x_cor = current_state['x']
            y_cor = current_state['y']

            #Moving the turtle to the position and write the name of the state
            pointer.goto(int(x_cor),int(y_cor))
            pointer.write(f"{user_input.title()}",align="center",font=("Arial",8,"normal"))

            #Append the state to the guessed list and increase the counter 
            guessed_list.append(user_input.title())
            state_count += 1 

if __name__ == "__main__":
    main()