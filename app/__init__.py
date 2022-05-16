from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY']='flask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manage.db'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)

from app import views