from flaskapp import app, db, bcrypt
from flaskapp.models import User, Student
from flaskapp.forms import LoginForm, RegistrationForm
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__, url_prefix='/auth',
                 template_folder='templates/auth')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password', category='error')
            return redirect(url_for('auth.login'))
        else:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('public.index'))
    return render_template('login.html', title='Login', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        RegistrationForm.register(form)
        flash(f'Registration Successful.')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('public.index'))


@auth.route('/profile/<int:user_id>')
@login_required
def profile():
    return render_template('account.html', title='Account')
