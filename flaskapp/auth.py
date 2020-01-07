from flaskapp import app, db
from flaskapp.forms import LoginForm
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user

bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    return render_template('register.html', title='Register', form=form)