from flask import Flask, render_template
from post import Post
import requests

#Getting the blogs json from the npoint API
BLOGS_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"
post_objects = []
response = requests.get(url=BLOGS_ENDPOINT)
all_blogs = response.json()

#Iterating through all the elements of json file and create objects of Post class
for blog in all_blogs:
    post_obj = Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

#Loading the homepage with all the blogposts title and subtitle
@app.route('/')
def home():
    return render_template("index.html",blog_posts=post_objects)

#Loading the body of the blog post requested by the user using read anchor tag
@app.route('/post/<blog_id>')
def get_blog(blog_id):
    return render_template("post.html",blog_id=int(blog_id),all_blogs=post_objects)

if __name__ == "__main__":
    app.run(debug=True)
