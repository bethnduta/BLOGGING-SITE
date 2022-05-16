from app import app
from flask import render_template,request
from app.data import Posts
from app.forms import RegisterForm
@app.route('/')
def hello():    
            return render_template('index.html')

@app.route('/posts')
def post():
    return render_template('post.html',posts=Posts)

@app.route('/blog')
def index():
    return render_template('macro.html')


    
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        
     return render_template('register.html', form=form)    
    