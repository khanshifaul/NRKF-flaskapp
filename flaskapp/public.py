from flaskapp import app
from flask import Blueprint, render_template, redirect, url_for, flash, request

bp = Blueprint('public', __name__, url_prefix='', template_folder='templates/public', static_folder='static')


@bp.route('/')
@bp.route('/home')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/academic')
def academic():
    return render_template('academic.html')


@bp.route('/admission')
def admission():
    return render_template('admission.html')


@bp.route('/facilities')
def facilities():
    return render_template('facilities.html')


@bp.route('/help')
def help():
    return render_template('help.html')


@bp.route('/contact')
def contact():
    return render_template('contact.html')


@bp.route('/notices')
def notices():
    return render_template('notices.html')


@bp.route('/student')
def student():
    return render_template('student.html')


@bp.route('/teacher')
def teacher():
    return render_template('teacher.html')