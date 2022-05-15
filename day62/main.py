from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired
# from datetime import datetime as class_dt
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe Name', validators=[DataRequired()])
    location_url = URLField(label='Location URL', validators=[DataRequired()])
    open_time = TimeField(label='Open Time', validators=[DataRequired()])
    close_time = TimeField(label='Close Time', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', validators=[DataRequired()],
     choices=['❌', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi_rating = SelectField(label='Wifi Rating', validators=[DataRequired()],
     choices=['❌', '📶', '📶📶', '📶📶📶', '📶📶📶📶', '📶📶📶📶📶'])
    power_outlet_rating = SelectField(label='Power Out Rating', validators=[DataRequired()],
     choices=['❌', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField(label='Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    # for POST method
    if form.validate_on_submit():
        new_cafe_entry = f'\n{form.cafe.data},{form.location_url.data},{form.open_time.data.strftime("%I:%M%p")},'\
                        f'{form.close_time.data.strftime("%I:%M%p")},{form.coffee_rating.data},{form.wifi_rating.data},'\
                        f'{form.power_outlet_rating.data}'
        with open('day62/cafe-data.csv', 'a', newline='', encoding='utf8') as csv_file:
            csv_file.write(new_cafe_entry)
        return redirect(url_for('cafes'))
    # for GET method
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('day62/cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
