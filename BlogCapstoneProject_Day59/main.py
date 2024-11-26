from flask import Flask,render_template,request
import requests
import smtplib
import dotenv

#Getting the environment variables
config = dotenv.dotenv_values("./.env")
email = config['EMAIL_ADD']
pswd = config['EMAIL_PSWD']
to_email = config['TO_EMAIL_ADD'] 

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
#And sending the details and message entered by the visitor through email
@app.route("/contact",methods=['GET','POST'])
def get_contact():
    if request.method == 'GET':
        content = "Contact Me"
        return render_template("contact.html",content=content)
    
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password=pswd)
            connection.sendmail(
                from_addr=email,
                to_addrs=to_email,
                msg=f"Subject:New Message\n\nName:{name}\nEmail:{mail}\nPhone:{phone}\nMessage:{message}"
            )

        content = "Successfully sent your message"
        return render_template("contact.html",content=content)

#Loading the each blog for user to read
@app.route("/blog/<blog_id>")
def show_post(blog_id):
    current_blog = blog_posts[int(blog_id)-1]
    return render_template("post.html", current_blog = current_blog)

if __name__ == "__main__":
    app.run(debug=True)