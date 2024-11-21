from flask import Flask
import random

app = Flask(__name__)

#Generating a random number between 0 and 9
number = random.randint(0,9)

#Initial page with a heading and gif
@app.route("/")
def initial_page():
    return "<h1> Guess a number between 0 and 9 </h1>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

#Getting the input from the user through url
#Generate a response accordingly, if guess is lower or higher or correct
@app.route("/<int:guess>")
def check(guess):
    if guess < number:
        return "<h1 style='color:red'>Too low, try again! </h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif guess > number:
        return "<h1 style='color:blue'>Too high, try again!</h1>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color:green'>You found me!</h1>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)