from flask import Flask, render_template, url_for, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegisterForm
from flask_bootstrap import Bootstrap

# Flask app creation
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'df51g564f2sd5fd4qss51de74f5d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///randopost.db'

# Database creation
db = SQLAlchemy(app)

# User registration setup
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# DB model creation
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

db.create_all()

# Route creation
@app.route('/')
def home():
    return render_template('index.html', page_name='home')

@app.route('/post')
def post():
    return render_template('index.html', page_name='post')

@app.route('/randos')
def randos():
    return render_template('index.html', page_name='randos')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('Email not found')
            return redirect(url_for('register'))
        elif form.password.data != user.password:
            flash('Incorrect password')
            return redirect(url_for('login'))
        else:
            flash('Successfully logged in')
            login_user(user)
            return redirect(url_for('home'))
    return render_template('index.html', page_name='login', form=form, user=current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit() and form.password.data == form.confirmation.data:
        new_user = User(
            email=form.email.data,
            password=form.password.data,
            name=form.name.data
        )
        if User.query.filter_by(email=new_user.email).first():
            flash('Email already exists')
            return redirect(url_for('login'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Successfully registered')
        return redirect(url_for('home'))
    return render_template('index.html', page_name='register', form=form, user=current_user)

@app.route('/logout')
def logout():
    logout_user()
    flash('Successfully logged out')
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html', page_name='about')

if __name__=='__main__':
    app.run(debug=True)