import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'BtIeWDcicUyTk8A1f7MvrMZRqH9k946d'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class Production(Config):
    DATABASE_URI = 'postgresql://localhost/database'


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
