from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from Flask_Bcrypt import Bcrypt

app = Flask(__name__)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'

