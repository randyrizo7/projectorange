import os

from flask import Flask, render_template, request, flash, redirect, session, g, abort
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import UserCreateForm, LoginForm, UserEditForm, PostForm
from models import db, connect_db, User, Post, Comment, Favorites, Follows


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///projectorange"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'

toolbar = DebugToolbarExtension(app)

connect_db(app)


API_BASE_URL = "https://api.spoonacular.com/recipes/findByNutrients"

key = "25e20deb25e947dd8192d0d89ccbea7d"

reponse = requests.get({API_BASE_URL}, params = {'apiKey': key, 'maxCarbs' : 30, 'number': 100 })

@app.route('/')
def signup():
    """ Handle User sign up """
    return render_template('base.html')

db.create_all()