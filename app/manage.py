import re
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/')
def blog():
    return render_template('blog.html')

@app.route('/index')
def index():
    return render_template('macro.html')

if __name__ == '__main__':
    app.run(debug=True)