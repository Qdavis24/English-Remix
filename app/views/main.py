import os
from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, send_file, abort
import datetime as dt
import secrets
from ..helpers import db_save_question, db_retrieve_questions, db_add_answers, db_delete_questions
from ..models import LlcComments, WcComments

TABLES = {"WcComments": WcComments, "LlcComments": LlcComments}

main_bp = Blueprint("main", __name__, "../templates")


def admin_protect(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        secret_key = request.form.get('secret_key') or request.args.get("secret_key")
        if not secret_key or not secrets.compare_digest(secret_key, os.environ.get('admin_key')):
            abort(404)
        return f(*args, **kwargs, secret_key=secret_key)

    return wrapper


@main_bp.route("/")
def index():
    grid_texts = [
        ["Campus Guide",
         "Navigating campus resources shouldn't add to your challenges as a nontraditional student. Your time and "
         "energy are invaluable, and your real-world experience enriches the classroom. Let us help you connect with "
         "resources to support your success."],

        ["Smart Investment",
         "Higher education is a major investment of time and energy. Maximize your return by utilizing free academic "
         "support services. As a nontraditional student, you've made sacrifices to be here; we're committed to helping "
         "you thrive."],

        ["Resource Access",
         "Accessing campus resources should be simple. This guide provides clear details on where to go, when services "
         "are available, and how to use them, so you can focus on succeeding in your studies without extra hassle."],

        ["Resource details",
         "Learn about essential campus services like the Writing Center and Lambda Learning Center. These guides "
         "include appointment scheduling and service details, giving you the confidence to achieve academic excellence."]
    ]

    card_texts = [
        "The Writing Center offers free support to Western students at any stage of the writing process, from "
        "brainstorming to final drafts. Writing consultants work with students in 25- or 50-minute sessions to help "
        "improve writing skills through constructive feedback, whether you're working on research papers, presentations,"
        " applications, or creative pieces.",
        "The Lambda Learning Center (LLC) is a collaborative space where students, tutors, and professors work together"
        " to master concepts in math, computer science, and engineering. Equipped with computers, whiteboards, and study"
        " spaces, the LLC provides both independent and group learning opportunities to help students succeed in their"
        " STEM courses."]

    return render_template("index.html", grid_texts=grid_texts, card_texts=card_texts)


@main_bp.route("/Lamda-Learning-Center")
def llc():
    questions = db_retrieve_questions(LlcComments)
    schedule = [
        ["Monday", "10:00 a.m. - 12:00 p.m., 2:00 p.m. - 6:00 p.m."],
        ["Tuesday", "10:00 a.m. - 12:00 p.m., 2:00 p.m. - 6:00 p.m."],
        ["Wednesday", "10:00 a.m. - 12:00 p.m., 2:00 p.m. - 6:00 p.m."],
        ["Thursday", "10:00 a.m. - 12:00 p.m., 2:00 p.m. - 6:00 p.m."],
        ["Friday", "10:00 a.m. - 12:00 p.m., 2:00 p.m. - 6:00 p.m."]
    ]
    services_grid = [
        ["Learning Environment",
         "The Lambda Learning Center (LLC) offers a collaborative space where students, tutors, and professors work"
         " together to master concepts, find academic success, and explore new ideas in STEM fields."],
        ["Equipped Facilities",
         "The LLC is furnished with computers, dry erase boards, math journals, STEM games, and plenty of room for "
         "individual or group work, all to facilitate engaged learning beyond the classroom."],
        ["Academic Support",
         "At the LLC, students can come to work independently on their homework or team up with classmates, fostering "
         "a community focused on supporting each other's academic achievements."],
        ["Accessible Hours",
         "The LLC is open Monday through Friday, from 10am to 12pm and 2pm to 6pm, providing ample opportunities for"
         " students to utilize the space and resources throughout the week."]
    ]
    location_card = """The LLC is located in the Rady Building at Western Colorado University. Specifically, it is in rooms
                      227, 229, and 231 of the Rady Building To find the LLC, you would need to go to the Rady Building
                      on the Western Colorado University campus. Once inside the Rady Building, you can look for rooms
                      227, 229, and 231, which is where the LLC is housed."""

    return render_template("llc.html", schedule=schedule, services_grid=services_grid,
                           location_card=location_card, questions=questions)


@main_bp.route("/LLC-submission", methods=["POST"])
def submit_llc():
    form_data = request.form.to_dict()
    db_save_question(name=form_data['name'], question=form_data['question'], table=LlcComments, date=dt.datetime.now())
    return redirect(url_for('main.llc'))


@main_bp.route("/Writing-Center")
def wc():
    questions = db_retrieve_questions(WcComments)
    schedule = [
        ["Sunday", "4:00 - 7:30 p.m."],
        ["Monday", "1:00 - 6:00 p.m."],
        ["Tuesday", "1:00 - 8:00 p.m."],
        ["Wednesday", "Noon - 8:00 p.m."],
        ["Thursday", "2:00 - 8:00 p.m."],
        ["Friday", "1:00 - 5:00 p.m."],
        ["Saturday", "CLOSED"]
    ]
    services_grid = [
        [
            "Writing Help",
            "The Writing Center offers in-person and online sessions, lasting 25 or 50 minutes, to support students"
            " at any stage of the writing process. Consultants provide feedback on brainstorming, revisions, research "
            "papers, presentations, applications, and creative work without simply editing papers."
        ],
        [
            "Workspace Access",
            "Located in Taylor 112D, the Writing Center provides a welcoming space for students to focus on writing. "
            "Equipped with handbooks, style guides, and online resources, it allows independent skill improvement with"
            " help available if needed."
        ],
        [
            "Essay Guidance",
            "The Writing Center helps students understand assignments, develop ideas, and plan essays. Consultants "
            "highlight strengths, suggest improvements, and teach self-editing techniques to build better writing "
            "habits for academic success."
        ],
        [
            "Flexible Hours",
            "Offering walk-in, scheduled, and online sessions, the Writing Center ensures accessibility with extensive"
            " hours six days a week. Evening weekday availability and Sunday hours accommodate diverse student "
            "schedules for convenient support."
        ]
    ]

    location_card = """The Writing Center is located in Taylor 112D at Western Colorado University's campus in Gunnison, 
                         CO. Students can find help at 1 Western Way, Gunnison, CO 81231. For questions or assistance, the
                         center can be reached by phone at 970.943.7079 or by email at writingcenter@western.edu. The
                         center is directed by Jennifer Foster Caldwell, M.A., who serves as both a Lecturer in English
                         and the Writing Center Director."""
    return render_template("wc.html", schedule=schedule, services_grid=services_grid,
                           location_card=location_card, questions=questions)


@main_bp.route("/WC-submission", methods=["POST"])
def submit_wc():
    form_data = request.form.to_dict()
    db_save_question(name=form_data['name'], question=form_data['question'], table=WcComments, date=dt.datetime.now())
    return redirect(url_for('main.wc'))


@main_bp.route("/Works-Cited")
def works_cited():
    path = "./static/works-cited.pdf"
    return send_file(path, mimetype="application/pdf", as_attachment=False)


@main_bp.route("/Admin")
@admin_protect
def admin(secret_key=None):
    questions = db_retrieve_questions(WcComments, LlcComments)
    print(questions)
    return render_template("admin.html", questions=questions, admin=True, secret_key=secret_key)


@main_bp.route("/Admin-Post", methods=["POST"])
@admin_protect
def admin_post(secret_key=None):
    form_data = request.form.to_dict()

    del form_data['secret_key']
    del form_data['csrf_token']

    to_add = []
    for key, value in form_data.items():
        table_name, table_id = key.split("-")
        answer = value
        to_add.append([TABLES[table_name], table_id, answer])
    print(to_add)
    db_add_answers(to_add)
    return redirect(url_for('main.admin', secret_key=secret_key))


@main_bp.route("/Delete-Question", methods=["POST"])
@admin_protect
def delete_questions(secret_key=None):
    form_data = request.form.to_dict()

    del form_data['secret_key']
    del form_data['csrf_token']

    to_delete = []
    for key, value in form_data.items():
        table_name, table_id = key.split("-")
        to_delete.append([TABLES[table_name], table_id])
    db_delete_questions(to_delete)
    return redirect(url_for('main.admin', secret_key=secret_key))
