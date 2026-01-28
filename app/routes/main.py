# app/routes/main.py
from flask import Blueprint, render_template, request

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("home.html")


@main_bp.route("/about")
def about():
    return render_template("about_us.html")


@main_bp.route("/contact", methods=['GET', 'POST'])
def contact():
    try:
        print(0)
    except print(0):
        pass
    
    if request.method == 'POST':
        print(request.form)
        
    return render_template("contact_us.html")
