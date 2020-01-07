from flaskapp import app, db, bcrypt
from flaskapp.models import User, Student
from flaskapp.forms import LoginForm, RegistrationForm
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__, url_prefix='/auth',
                 template_folder='templates/auth')


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('public.index'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
        else:
            pass
    return render_template('login.html', title='Login', form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('public.index'))


@auth.route("/account")
def account():
    return render_template('account.html', title='Account')


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
