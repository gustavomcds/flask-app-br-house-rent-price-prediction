"""Flask configuration."""

from os import environ, path
from dotenv import load_dotenv, dotenv_values

basedir = path.abspath(path.dirname(__file__))
dotenv_values(path.join(basedir, '.env'))


class Config:
    """Base config."""

    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class ProdConfig(Config):
    """Production config."""
    
    FLASK_ENV = 'production'
    TESTING = False

class DevConfig(Config):
    """Development config."""

    FLASK_ENV = 'development'
    TESTING = True