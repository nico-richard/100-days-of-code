from urllib import response
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-list.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

movie_db_api_key = "9d2c939718d281ff45061117c43b057a"
url_image_prefix = "https://image.tmdb.org/t/p/w500"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.Text, nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self) -> str:
        return f"Movie {self.id} : {self.title}, rank : {self.ranking}"


class EditMovieForm(FlaskForm):
    rating = FloatField(label="Rating", validators=[DataRequired()])
    review = StringField(label="Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired()])
    submit = SubmitField(label="Done")


def get_movie_list(movie_title):
    params = {
        "api_key": movie_db_api_key,
        "query": movie_title,
    }
    response = requests.get(
        url="https://api.themoviedb.org/3/search/movie", params=params
    )
    data = response.json()
    movie_list = data["results"]
    return movie_list


def get_movie_details(movie_id):
    params = {
        "api_key": movie_db_api_key,
    }
    response = requests.get(
        url=f"https://api.themoviedb.org/3/movie/{movie_id}", params=params
    )
    data = response.json()
    return data


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit_movie():
    form = EditMovieForm()
    movie_id = request.args.get("id")
    movie_to_edit = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_edit.rating = float(form.rating.data)
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie_to_edit)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        movie_list = get_movie_list(title)
        return render_template("select.html", movies=movie_list)
    return render_template("add.html", form=form)


@app.route("/find_details")
def add_movie_from_api():
    movie_id = request.args.get("id")
    data = get_movie_details(movie_id)
    new_movie = Movie(
        title=data["original_title"],
        year=int(data["release_date"].split("-")[0]),
        description=data["overview"],
        img_url=str(url_image_prefix + data["poster_path"]),
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit_movie", id=new_movie.id))


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
    # new_movie = Movie(
    #     title="The dictator",
    #     year=2012,
    #     description="L'Amiral Général Aladeen règne sur un petit pays du nord de l'Afrique nommé Wadiya. Il prétend aimer son peuple mais n'hésite pas à faire exécuter quiconque le contredit. Lors d'un voyage à New York, il est trahi par son oncle et conseiller qui le remplace par une doublure qu'il peut contrôler à sa guise.",
    #     rating=8.8,
    #     ranking=9,
    #     review="Sacha Baron Cohen",
    #     img_url="https://fr.web.img6.acsta.net/medias/nmedia/18/84/77/28/20096200.jpg"
    # )
    # db.session.add(new_movie)
    # db.session.commit()
