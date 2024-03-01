'''
Flask App configuration
'''
from os import environ, path
from dotenv import load_dotenv

BASEDIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASEDIR, '.env'))

class Config:
    '''
    Base config
    '''
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    '''
    Production config
    '''
    FLASK_ENV = "production"
    FLASK_DEBUG = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    '''
    Development config
    '''
    FLASK_ENV = "development"
    FLASK_DEBUG = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')