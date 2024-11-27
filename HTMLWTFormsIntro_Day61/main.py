from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import dotenv

#Getting the environment variables
config = dotenv.dotenv_values("./.env")

#Creating class for creating For,
class MyForm(FlaskForm):
    email = StringField(label = 'Email')
    password = PasswordField(label = 'Password')
    submit = SubmitField(label = 'Log In')

app = Flask(__name__)
app.secret_key = config['APP_SECRETKEY']

#Loading the homepage
@app.route("/")
def home():
    return render_template('index.html')

#Loading the login page
@app.route("/login",methods=['GET','POST'])
def login():
    login_form = MyForm()
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
