from flask import Blueprint, render_template

solutions_bp = Blueprint("solutions", __name__)

@solutions_bp.route("/")
def solutions_index():
    return render_template("solutions/index.html")

@solutions_bp.route("/infrastructure")
def infrastructure():
    return render_template("solutions/infrastructure.html")

@solutions_bp.route("/software")
def software():
    return render_template("solutions/software.html")

@solutions_bp.route("/ai")
def ai_solutions():
    return render_template("solutions/ai.html")

@solutions_bp.route("/security")
def security():
    return render_template("solutions/security.html")
