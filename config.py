import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'BtIeWDcicUyTk8A1f7MvrMZRqH9k946d'
    DATABASE_URI = 'sqlite:///:memory:'


class Production(Config):
    DATABASE_URI = 'postgresql://localhost/database'


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
