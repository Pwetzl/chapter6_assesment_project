from app import app
from flask import render_template


@app.route('/')
@app.route('/shop')
def index():
    """shop URL"""
    return render_template("index.html" , title='index page')


@app.route('/register')
def register():
    """register URL"""
    return render_template('register.html', title='register')


@app.route('/login')
def login():
    """login URL"""
    return render_template('login.html', title='login')