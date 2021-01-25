from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from wtforms_alchemy import ModelForm

bcrypt = Bcrypt()
db = SQLAlchemy()



class User(db.Model):
    """Users in app"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.Text, nullable= False)

    last_name = db.Column(db.Text, nullable=False)

    email = db.Column(db.Text, nullable= False, unique=True)

    username = db.Column(db.Text, nullable=False, unique=True) 

    password = db.Column(db.Text, nullable= False)

    image_url = db.Column(db.Text)

    bio = db.Column(db.Text)





class Post(db.Model):
    """A user will Post a their comment to about a recipe to a timeline"""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)

    text =  db.Column(db.String(300), nullable = False)

    timestamp = db.Column(db.Datetime, nullable=False, default= datetime.utcnow())

    meal_id = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

class Comment(db.Model):
    """Other users can leave a comment on the post """

    __tablename__='comments'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    post_id = db.Column(db.ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)

    comment =  db.Column(db.String(300), nullable = False)

    timestamp = db.Column(db.Datetime, nullable=False, default= datetime.utcnow())

class Favorites(db.Model):
    """ Mapping meal likes to users"""

    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))

    meal_id = db.Column(db.Integer, nullable=False)

class Follows(db.Model):
    """Connection to which user is following and which user is being followed"""

    __tablename__ = 'follows'

    user_being_followed_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete="cascade"),
        primary_key=True,
    )

    user_following_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete="cascade"),
        primary_key=True,
    )


