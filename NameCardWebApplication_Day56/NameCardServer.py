from flask import Flask,render_template

app = Flask(__name__)

#Rendering the index html file from html5up's template
@app.route("/")
def Hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)