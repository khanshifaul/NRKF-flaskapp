import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'BtIeWDcicUyTk8A1f7MvrMZRqH9k946d'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


class Production(Config):
    DATABASE_URI = 'postgres://unzxbywmkcyuwt:112ab4fbbf7b5cb90b4799fb2e9b9ee146a5583194c6bda4a263c31f1882379c@ec2-174-129-33-88.compute-1.amazonaws.com:5432/d4886fqji3ve0k'

class Staging(Config):
    DEBUG = True
    DATABASE_URI = 'postgres://unzxbywmkcyuwt:112ab4fbbf7b5cb90b4799fb2e9b9ee146a5583194c6bda4a263c31f1882379c@ec2-174-129-33-88.compute-1.amazonaws.com:5432/d4886fqji3ve0k'



class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
