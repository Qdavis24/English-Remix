import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI")

