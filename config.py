from dotenv import load_dotenv
from os import path, environ


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))



class Config(object):
    DEBUG = False
    TESTING = False
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class Production(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False


class Development(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
