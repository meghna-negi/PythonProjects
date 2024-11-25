from flask import Flask,render_template
import requests

app = Flask(__name__)

#Retrieving the blog posts from the API
BLOG_ENDPOINT = " https://api.npoint.io/d6864154b43938a52176"
blog_posts = requests.get(url=BLOG_ENDPOINT).json()

#Loading the home page
@app.route("/")
def home():
    return render_template("index.html", all_blogs=blog_posts)

#Loading the about page
@app.route("/about")
def get_about():
    return render_template("about.html")

#Loading the contact details page with the form
@app.route("/contact")
def get_contact():
    return render_template("contact.html")

#Loading the each blog for user to read
@app.route("/blog/<blog_id>")
def show_post(blog_id):
    current_blog = blog_posts[int(blog_id)-1]
    return render_template("post.html", current_blog = current_blog)

if __name__ == "__main__":
    app.run(debug=True)