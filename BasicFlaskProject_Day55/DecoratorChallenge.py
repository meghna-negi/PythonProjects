from flask import Flask

app = Flask(__name__)

#Decorator to make the text bold
def make_bold(function):
    def wrapper_function():
        return '<b>'+ function() + '</b>'
    return wrapper_function

#Decorator to make text emphasized
def make_emphasis(function):
    def wrapper_function():
        return '<em>'+ function() + '</em>'
    return wrapper_function

#Decorator to underline the text
def make_underlined(function):
    def wrapper_function():
        return '<u>'+ function() + '</u>'
    return wrapper_function

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)