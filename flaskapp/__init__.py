from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config



app = Flask(__name__,instance_relative_config=True)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = ('Please log in to access this page.')
from flaskapp import public
app.register_blueprint(public.bp)
from flaskapp import auth
app.register_blueprint(auth.auth)
app.add_url_rule('/login', endpoint='index')