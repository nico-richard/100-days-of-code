from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

WTF_CSRF_ENABLED = False

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.secret_key = 'akey'

    return app

app = create_app()

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField(label='Log In')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/boot")
def bootstrap_html():
    login_form = LoginForm()
    return render_template('from_bootstrap.html', form=login_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    
    if request.method == 'POST':
        if login_form.validate_on_submit():
            return render_template('success.html')
        else:
            return render_template('denied.html')
        
    return render_template('login.html', form=login_form)


@app.route('/submit')
def submit():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)