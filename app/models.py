from . import db
from sqlalchemy import DateTime


class LlcComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(DateTime, unique=False, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    question = db.Column(db.String(350), unique=False, nullable=False)
    answer = db.Column(db.String(350), unique=False, nullable=True)


class WcComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(DateTime, unique=False, nullable=False)
    name = db.Column(db.String(100), unique=False, nullable=False)
    question = db.Column(db.String(350), unique=False, nullable=False)
    answer = db.Column(db.String(350), unique=False, nullable=True)
