from flask import Flask,render_template,request

app = Flask(__name__)

#Loading the homepage
@app.route("/")
def home():
    return render_template("index.html")

#Loading the page thaat displays the input entered by user through a form
@app.route("/login",methods=['POST'])
def logged_in():
    username = request.form['username']
    password = request.form['password']
    return render_template("display.html",username=username,password=password)

if __name__ == "__main__":
    app.run(debug=True)