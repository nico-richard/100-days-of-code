from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, SubmitField, PasswordField, DateField, FileField
from wtforms.validators import DataRequired
from flask_uploads import UploadSet, IMAGES

photos = UploadSet('photos', IMAGES)

class RegisterForm(FlaskForm):
    name = StringField(label='Username', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    confirmation = PasswordField(label='Confirmation', validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class PostForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    refer_date = DateField(label='Date', validators=[DataRequired()])
    image = FileField(label='Image', validators=[FileAllowed(photos, 'Image only')])
    description = StringField(label='Description')
    submit = SubmitField(label='Submit')
    