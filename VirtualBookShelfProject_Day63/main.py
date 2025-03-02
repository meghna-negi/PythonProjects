from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    rating: Mapped[float]

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    result = db.session.execute(db.select(books).order_by(books.title))
    all_books = result.scalars()
    print(all_books)
    return render_template("index.html",books=all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    if request.method == "POST":
        book = books(
            title = request.form["title"],
            author = request.form["author"],
            rating = request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(books, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(books, book_id)
    return render_template("edit.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    book_to_delete = db.get_or_404(books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)