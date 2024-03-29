from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user



@app.route('/')
@app.route('/index')
@login_required
def index():
    
    user = {'username': 'Thandi'}
    posts = [
        {
            'author': {'username': 'Olwethu'},
            'body': 'Brown skin girl'
        },
        {
            'author': {'username': 'Anathi'},
            'body': 'I just cant wait to be king'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # flash('login requested for user: {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout()
    logout_user()
    return redirect(url_for('index'))