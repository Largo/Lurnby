from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, URL, ValidationError, Email, EqualTo, Length
from app.models import User

class URLForm(FlaskForm):
    url = URLField('URL', validators=[DataRequired(), URL()])
    submit = SubmitField('Get Content')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('First name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[EqualTo('password')])
    submit = SubmitField('Sign In')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data.lower()).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data.lower()).first()
        if user is not None:
            raise ValidationError('Please use a different email')

class AddTopicForm(FlaskForm):
    title = StringField('Topic title ...', validators=[DataRequired()])

class AddHighlightForm(FlaskForm):
    text = TextAreaField('Highlight')
    note = TextAreaField('Note')
    