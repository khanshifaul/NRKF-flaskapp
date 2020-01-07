from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.Development')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.category = 'info'
login_manager.blueprint_login_views='login'


from flaskapp import public
app.register_blueprint(public.bp)

from flaskapp import auth
app.register_blueprint(auth.auth)
app.add_url_rule('/login', endpoint='index')

# def create_db():
#     db.create_all()
