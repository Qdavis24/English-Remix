from . import db


def db_save_question(name, question, date, table: db.Model):
    question = table(name=name, question=question, date=date)
    db.session.add(question)
    db.session.commit()


def db_retrieve_questions(*args):
    questions = []
    for table in args:
        questions += [[row.name, row.question, row.answer, row.id,
                       table.__name__.split(".")[-1].split("'")[0]] for
                      row in table.query.all()]
    return questions


def db_add_answers(to_add):
    for package in to_add:
        row = package[0].query.get(package[1])
        row.answer = package[2]
    db.session.commit()


def db_delete_questions(to_delete):
    for package in to_delete:
        row = package[0].query.get(package[1])
        db.session.delete(row)
    db.session.commit()
