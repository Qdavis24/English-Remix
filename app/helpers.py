from . import db


def save_question(name, question,date, table: db.Model):
    question = table(name=name, question=question, date=date)
    db.session.add(question)
    db.session.commit()


def retrieve_questions(table: db.Model):
    comments = [[row.name, row.question, row.answer] for row in table.query.all()]
    return comments
