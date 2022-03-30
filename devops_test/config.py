import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    extend_existing=True
    #Database URL
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    extend_existing=True
