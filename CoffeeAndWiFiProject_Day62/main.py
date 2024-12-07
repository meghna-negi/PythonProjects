from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap=Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    locURL = StringField('Cafe Location on Google Maps (URL)', validators=[URL(message='Invalid URL')])
    openTime = StringField('Opening Time e.g. 8AM')
    closeTime = StringField('Closing Time e.g. 5:30PM')
    coffeeRating = SelectField(u'Coffee Rating', choices=[('1','☕'), ('2','☕☕'), ('3','☕☕☕'), ('4','☕☕☕☕'), ('5','☕☕☕☕☕')])
    wifiRating = SelectField(u'Wifi Strength Rating', choices=[('0','✘'),('1','💪'),('2','💪💪'),('3','💪💪💪'),('4','💪💪💪💪'),('5','💪💪💪💪💪')])
    powerRating = SelectField(u'Power Socket Availability', choices=[('0','✘'),('1','🔌'),('2','🔌🔌'),('3','🔌🔌🔌'),('4','🔌🔌🔌🔌'),('5','🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = f'{form.cafe.data},{form.locURL.data},{form.openTime.data},{form.closeTime.data},{form.coffeeRating.data},{form.wifiRating.data},{form.powerRating.data}'
        print(new_row)
        with open('cafe-data.csv',mode='a') as file:
            file.write(new_row)
            file.write("\n")
            
    
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
