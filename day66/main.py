from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def __repr__(self) -> str:
        return f'{self.id}\n{self.name}\n{self.location}\n{self.seats}\n{self.has_toilet}\n'\
               f'{self.has_wifi}\n{self.has_sockets}\n{self.can_take_calls}\n{self.coffee_price}'\

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route('/random')
def random():
    cafe = Cafe.query.get(randint(0,21))
    # return f'{cafe.__dict__}'
    return f'{cafe}'


@app.route('/all')
def all():
    cafes = db.session.query(Cafe).all()
    cafes_list = {'cafes': [cafe.to_dict() for cafe in cafes]}
    # for element in cafes:
        # cafe = {column.name: element.__getattribute__(column.name) for column in Cafe.__table__.columns}
        # cafes_list['cafes'].append(cafe)
    return cafes_list


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
