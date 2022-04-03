from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

print(path.abspath(path.dirname(__file__)))
print(load_dotenv(path.join(basedir, '.env')))

# generic flask setting
TESTING = True
FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
print(environ.get('SQLALCHEMY_DATABASE_URI'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
