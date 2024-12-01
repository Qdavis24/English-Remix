from . import db


class LlcComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    comment = db.Column(db.String(350), unique=False, nullable=False)


class WcComments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    comment = db.Column(db.String(350), unique=False, nullable=False)
