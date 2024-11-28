from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,Length
import dotenv

#Getting the environment variables
config = dotenv.dotenv_values("./.env")

#Creating class for creating Form
#Validations should be done to check if the email address is valid or not and if password is atleat 8 characters long
class MyForm(FlaskForm):
    email = StringField(label = 'Email', validators=[DataRequired(),Email('Invalid email address.')])
    password = PasswordField(label = 'Password', validators=[DataRequired(), Length(min=8,message='Field must be at least 8 characters long.')])
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
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
