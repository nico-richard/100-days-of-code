import string
from random import choice, randint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

# db.create_all()

def gen_word():
    count = 1
    while count <= 10:
        letters = [choice(string.ascii_lowercase) for letter in range(7)]
        word = ''.join(letters)
        yield word
        count += 1

# for word in gen_word():
#     db.session.add(Book(title=word, author=word, rating=randint(0, 10)))
#     db.session.commit()

all_books = db.session.query(Book).all()
for book in all_books:
    print(book.title)

# book = Book.query.filter_by(title='owebaib')
# print(book)
