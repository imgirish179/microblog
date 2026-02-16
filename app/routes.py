from flask import flash, redirect, render_template, url_for
from app import app
from app.forms import MyForm

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
    return render_template('index.html', title="Dashboards", user={'username': 'Guest'}, tests="TesTS")

@app.route('/posts')
def posts():
    user = {'username': 'Guest'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('posts.html', title='Posts', user=user, posts=posts)

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/testform', methods=['GET', 'POST'])
def testform():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        flash('Form submitted successfully! Name: {}'.format(name))
        # return redirect(url_for('contact', title='Contact'))
    return render_template('form.html', title='Test Form', form=form)