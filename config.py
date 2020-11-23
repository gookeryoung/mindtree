import os

DIR_BASE = os.path.abspath(os.path.dirname(__file__))
DIR_TEMPLATES = os.path.join(DIR_BASE, 'templates')
DIR_STATIC = os.path.join(DIR_BASE, 'static')
DIR_TEST = os.path.join(DIR_BASE, 'test')

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
