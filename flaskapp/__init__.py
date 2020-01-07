from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from Flask_Bcrypt import Bcrypt

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Development')


db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'

from flaskapp import public
app.register_blueprint(public.bp)


from flaskapp import auth
app.register_blueprint(auth.bp)
