from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = 'kllkRfgd946KJU9fk4r6l09i4D5lkm489'

REMEMBER_COOKIE_DURATION = timedelta(days=5)
