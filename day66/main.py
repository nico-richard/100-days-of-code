from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_KEY = 'azerty'


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


    def __repr__(self):
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
    return cafe.to_dict()
    # return f'{cafe}'


@app.route('/all')
def all():
    cafes = Cafe.query.all()
    return {'cafes': [cafe.to_dict() for cafe in cafes]}


@app.route('/search')
def search():
    location = request.args['loc'].capitalize()
    cafes = Cafe.query.filter_by(location=location).first()
    if cafes:
        return jsonify(cafe=cafes.to_dict())
    else:
        return jsonify(error={"Not found": "Sorry we have not found any cafe at this location"})


@app.route('/search-id/<int:cafe_id>')
def search_by_id(cafe_id):
    cafes = Cafe.query.get(cafe_id)
    if cafes:
        return jsonify(cafe=cafes.to_dict())
    else:
        return jsonify(error={"Not found": "Sorry we have not found this cafe id"})


@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    location = request.form.get('location')
    map_url = request.form.Get('map_url')
    new_cafe = Cafe(name=name, location=location, map_url=map_url)
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe", "new cafe": new_cafe.to_dict()})


@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get('price')
    cafe_to_update = Cafe.query.get(cafe_id)

    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated cafe price", "new cafe": cafe_to_update.to_dict()}), 200
    else:
        return jsonify(error={"not found": "Sorry we have not found this cafe id"}), 404


@app.route('/report-close/<int:cafe_id>', methods=['DELETE'])
def report_close(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    api_key = request.args.get('API_KEY')
    
    if api_key == API_KEY:
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted cafe"}), 200
        else:
            return jsonify(error={"not found": "Sorry we have not found this cafe id"}), 404
    else:
        return jsonify(error="Wrong api key"), 403


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
