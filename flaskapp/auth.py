from flaskapp import app, db, bcrypt
from flaskapp.models import User, Student
from flaskapp.forms import LoginForm, RegistrationForm
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required

bp = Blueprint('auth', __name__, url_prefix='/auth',
               template_folder='templates/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('dbmanage'))
        return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'registerd')
    return render_template('register.html', title='Register', form=form)
