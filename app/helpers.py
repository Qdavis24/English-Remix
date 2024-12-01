from . import db


def save_comment(name, message, table: db.Model):
    comment = table(name=name, comment=message)
    db.session.add(comment)
    db.session.commit()


def retrieve_comments(table: db.Model):
    comments = [[row.name, row.comment] for row in table.query.all()]
    return comments
