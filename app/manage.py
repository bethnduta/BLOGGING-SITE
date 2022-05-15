from flask import Flask, render_template, flash, redirect,url_for,session,logging
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField,TextAreaField,PasswordField,validators
from passlib import sha256_crypt

# from data import Posts

app = Flask(__name__)
# posts = Posts()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manage.db'
# db = SQLAlchemy(app)

# class Blog(db.Model):
#     id = db.Column(db.Integer(), primay_key=True)
#     name = db.Column(db.String(length=30), nullable=False, unique=True)
#     title = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.String(length=1024), nullable=False, unique=True)

@app.route('/')
def hello():    
            return render_template('index.html')

@app.route('/posts')
def post():
    return render_template('post.html')

@app.route('/blog')
def index():
    return render_template('macro.html')

if __name__ == '__main__':
    app.run(debug=True)