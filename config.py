import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = '123QWE'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    
