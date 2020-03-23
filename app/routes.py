from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Joacim'}
    posts = [
        {
            'author': {'username': 'Joacim'},
            'body': 'Vacker dag i Järna'
        },
        {
            'author': {'username': 'Louise'},
            'body': 'Vacker dag i Gnesta'
        }
    ]

    return render_template('index.html', title='Hello', user=user, posts=posts)