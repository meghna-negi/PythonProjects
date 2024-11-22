from flask import Flask,render_template
import requests

GENDERIZE_ENDPOINT = "https://api.genderize.io"
AGEIFY_ENDPOINT = "https://api.agify.io"

app = Flask(__name__)

#Loading homepage
@app.route("/")
def hello():
    return "Hello"

#Loading the page for the user
#Getting the given name's age and gender from the APIs and displaying the html page
@app.route("/<name>")
def name_info(name):
    gender_response = requests.get(url=f'{GENDERIZE_ENDPOINT}?name={name}')
    gender = gender_response.json()["gender"]
    
    age_response = requests.get(url=f'{AGEIFY_ENDPOINT}?name={name}')
    age = age_response.json()["age"]

    return render_template("index.html",username=name.title(),namegender=gender,nameage=age)

if __name__ == "__main__":
    app.run(debug=True)