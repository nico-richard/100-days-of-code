from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
WTF_CSRF_ENABLED = False

app = Flask(__name__)

class MyForm(FlaskForm):
    name = StringField('name')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm(meta={'csrf': False})
    if form.validate_on_submit():
        return redirect('login')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)