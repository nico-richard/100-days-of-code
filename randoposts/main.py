from flask import Flask, render_template, url_for, redirect, flash
from flask_login import LoginManager, login_user, current_user, logout_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegisterForm, PostForm, photos
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_uploads import configure_uploads

# Flask app creation
app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'df51g564f2sd5fd4qss51de74f5d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///randopost.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOADED_PHOTOS_DEST'] = 'static/images'

# Database creation
db = SQLAlchemy(app)

# Upload image tool
configure_uploads(app, photos)

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
    image = db.Column(db.LargeBinary)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.Text)

    def __repr__(self) -> str:
        return f'Post {self.id} : {self.title} at {self.creation_date} from {self.author}\n'

# db.drop_all()
# db.create_all()

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

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        filename = photos.save(form.image.data)
        # file_url = photos.url(filename)
        new_post = Post(
        title = form.title.data,
        author = current_user.id,
        refer_date = form.refer_date.data,
        # image = filename,
        description = form.description.data,
        )
        db.session.add(new_post)
        db.session.commit()
        flash('new post added')
        return redirect(url_for('home'))
    else:
        filename = None
    return render_template('index.html', page_name='post', form=form)

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

@app.route('/get_db', methods=['POST'])
def get_db():
    all_users = User.query.all()
    all_posts = Post.query.all()
    data = [all_users, all_posts]
    return render_template('index.html', db_data=data, page_name='DB details')

if __name__=='__main__':
    app.run(debug=True)