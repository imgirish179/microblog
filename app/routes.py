from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/home')
def home():
    user = {'username': 'Guest'}
    return '''
        <html>
            <head>
                <title>Home Page</title>
            </head>
            <body>
                <h1>Welcome, ''' + user['username'] + '''!</h1>
            </body>
        </html>
    '''

@app.route('/dashboard')
def dashboard():
    return render_template('index.html', title='Dashboard', user={'username': 'Guest'})

@app.route('/helloworld')
def about():
    return 12

@app.route('/')
def contact():
    return "Contact Page"



