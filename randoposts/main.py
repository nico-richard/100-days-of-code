import os
from flask import Flask, render_template, url_for, redirect, flash, request, session
from flask_login import LoginManager, login_user, current_user, logout_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegisterForm, PostForm, photos
from flask_bootstrap import Bootstrap
from datetime import datetime
from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))

# Flask app creation
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'df51g564f2sd5fd4qss51de74f5d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///randopost.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static', 'images')
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}

# Database creation
db = SQLAlchemy(app)

# DB model creation


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    posts = db.relationship('Post', backref='user')

    def __repr__(self) -> str:
        return f'User {self.id} : {self.name}, {self.email} has written {self.posts}\n'


class Post(UserMixin, db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    refer_date = db.Column(db.DateTime)
    image = db.Column(db.String(100))
    likes = db.Column(db.Integer, default=0)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text)

    def __repr__(self) -> str:
        return f'Post {self.id} : {self.title} at {self.creation_date} from user {self.author}\n'

# db.drop_all()
# db.create_all()

# db.session.execute('ALTER TABLE post ADD likes INTEGER')


# User registration setup
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Route creation


@app.route('/')
def home():
    return render_template('index.html', page_name='home')


@app.route('/add_like/<int:post_id>')
def add_like(post_id):
    post_to_like = Post.query.get(post_id)
    post_to_like.likes += 1
    db.session.commit()
    return redirect(url_for('all_posts'))


@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        file = request.files['upload_input']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        session['uploaded_img_file_path'] = os.path.join(
            app.config['UPLOAD_FOLDER'], filename)
    return render_template('index.html', page_name='upload')


@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if request.method == 'POST':
        if current_user.is_authenticated:
            file = request.files['image']
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], filename))
                session['uploaded_img_file_path'] = os.path.join(
                    app.config['UPLOAD_FOLDER'], filename)
            else:
                filename = None
            new_post = Post(
                title=form.title.data,
                author=current_user.id,
                refer_date=form.refer_date.data,
                image=filename,
                description=form.description.data,
            )
            db.session.add(new_post)
            db.session.commit()
            flash('new post added')
            return redirect(url_for('home'))
        else:
            flash('Please first authenticate')
    return render_template('index.html', page_name='post', form=form)


@app.route('/my_posts')
def my_posts():
    posts = Post.query.filter_by(author=current_user.id).all()
    return render_template('index.html', page_name='my_posts', posts=posts)


@app.route('/all_posts')
def all_posts():
    posts = Post.query.all()
    return render_template('index.html', page_name='all_posts', posts=posts)


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


@app.route('/get_db', methods=['POST'])
def get_db():
    all_users = User.query.all()
    all_posts = Post.query.all()
    data = [all_users, all_posts]
    return render_template('index.html', db_data=data, page_name='DB details')


@app.route('/delete_post/<int:post_id>')
def delete_post(post_id):
    post_to_del = Post.query.get(post_id)
    db.session.delete(post_to_del)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
