from flask import Blueprint, render_template

index_bp = Blueprint("index", __name__, "../templates")


@index_bp.route("/")
def index():
    texts = ["Whether you're returning to education after years in the workforce, juggling family responsibilities, or transitioning from military service, navigating campus resources shouldn't add to your challenges. As a nontraditional student, your time and energy are invaluable assets in your educational journey. Your wealth of real-world experience brings unique perspectives to the classroom - let us help you connect with the resources you need to succeed.",
             "Your investment in higher education goes beyond tuition - it's an investment of your hard-earned time and energy. Our guide helps you maximize your return by connecting you with free academic support services that can make the difference between struggling alone and thriving with expert guidance. As a nontraditional student, you've likely made significant sacrifices to be here; we're dedicated to helping you make the most of these valuable resources.",
             "Finding and accessing campus resources shouldn't require detective work, especially when you're juggling multiple responsibilities outside of school. This guide provides clear, straightforward information about where to go, when services are available, and exactly how to access the support you need. We've streamlined the process of connecting you with academic resources so you can spend less time searching and more time succeeding in your studies.",
             "Below you'll find detailed information about two essential campus resources: the Writing Center and the Lambda Learning Center. Each card provides everything you need to know about these services - from scheduling appointments to what to expect during your visit. As a nontraditional student, you've already taken the brave step of returning to education; we're here to help you take the next step toward academic excellence with confidence and clarity."]
    return render_template("index.html", texts=texts)
