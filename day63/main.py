from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from random import choice, randint
import string


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=True)
    author = db.Column(db.String(250), nullable=True)
    rating = db.Column(db.Integer, nullable=True)

    def __repr__(self) -> str:
        return f'Book {self.id} : {self.title}, {self.author}, {self.rating}'


def gen_word():
    count = 1
    while count <= 10:
        letters = [choice(string.ascii_lowercase) for letter in range(7)]
        word = ''.join(letters)
        yield word
        count += 1


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        db.session.add(Book(title=title, author=author, rating=rating))
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/delete')
def list_del():
    all_books = db.session.query(Book).all()
    return render_template('delete.html', books=all_books)


if __name__ == "__main__":
    app.run(debug=True)

