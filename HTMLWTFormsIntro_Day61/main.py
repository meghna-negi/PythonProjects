from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
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
bootstrap = Bootstrap5(app)

#Loading the homepage
@app.route("/")
def home():
    return render_template('index.html')

#Loading the login page
#Validating the form and load success page only when condition is satisfied
@app.route("/login",methods=['GET','POST'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if(login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678'):
            return render_template('success.html')
        else:
             return render_template('denied.html')

    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
